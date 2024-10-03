from rest_framework import viewsets, generics
from home.models import Allocation, Period
from qrscan.models import MessCard, Meal
from .serializers import AllocationSerializer, PeriodSerializer, AllocationDetailSerializer, QRVerifySerializer, MealSerializer, UserSerializer, QRVerifyPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .permissions import IsStaff
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .utils.rebate_checker import is_student_on_rebate

class LogoutView(APIView):
    permission_classes = [IsStaff]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        

class IsAuthenticated(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        if request.user.is_staff:
            return Response({"detail": "Authenticated"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        

class UserDetail(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class AllocationViewSet(viewsets.ReadOnlyModelViewSet):    
    permission_classes = [IsStaff]
    serializer_class = AllocationSerializer
    queryset = Allocation.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AllocationSerializer 
        elif self.action == 'retrieve':
            return AllocationDetailSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        period_id = self.request.query_params.get('period_id')
        if period_id:
            return Allocation.objects.filter(period_id=period_id)
        else:
            return Allocation.objects.filter()
    

class PeriodViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsStaff]
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

    def get_queryset(self):
        return Period.objects.order_by('-start_date')[:1]
    

class QRVerifyView(generics.RetrieveAPIView):
    permission_classes = [IsStaff]
    serializer_class = QRVerifySerializer
    queryset = MessCard.objects.all()
    lookup_field = 'id'


class QRVerifyUpdateView(APIView):
    permission_classes = [IsStaff]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_STRING, description='Card ID')
            },
            required=['id'],
        ),
        responses={200: 'Meal recorded successfully', 400: 'Invalid card id or bad request', 400: 'Meal already recorded.'}
    )

    def post(self, request):
        data = request.data

        serializer_data = {
            "id": data['id']
        }
        serializer = QRVerifyPostSerializer(data=serializer_data)
        if serializer.is_valid():
            card_id = serializer.validated_data['id']
            try:
                card = MessCard.objects.get(id=card_id)
                date = timezone.localtime().date()
                time = timezone.localtime().time()

                is_rebate = is_student_on_rebate(card.student, card.allocation)

                if is_rebate:
                    return Response({"detail": "Student is on rebate."}, status=status.HTTP_400_BAD_REQUEST)

                # Time in UTC

                if time < timezone.datetime.strptime('11:00:00', '%H:%M:%S').time():
                    meal_type = 'breakfast'
                elif time < timezone.datetime.strptime('15:00:00', '%H:%M:%S').time():
                    meal_type = 'lunch'
                else:
                    meal_type = 'dinner'

                meal, _ = Meal.objects.get_or_create(mess_card=card, date=date)

                if meal_type == 'breakfast':
                    if(meal.breakfast):
                        return Response({"detail": "Meal already recorded."}, status=status.HTTP_400_BAD_REQUEST)
                    meal.breakfast = True
                elif meal_type == 'lunch':
                    if(meal.lunch):
                        return Response({"detail": "Meal already recorded."}, status=status.HTTP_400_BAD_REQUEST)
                    meal.lunch = True
                elif meal_type == 'dinner':
                    if(meal.dinner):
                        return Response({"detail": "Meal already recorded."}, status=status.HTTP_400_BAD_REQUEST)
                    meal.dinner = True

                meal.save()
                return Response({"detail": "Meal recorded successfully."}, status=status.HTTP_200_OK)
            except MessCard.DoesNotExist:
                return Response({"detail": "Invalid card id."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaff]
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
