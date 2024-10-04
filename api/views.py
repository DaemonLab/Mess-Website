from django.utils import timezone
from rest_framework import viewsets, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from home.models import Allocation, Period
from qrscan.models import MessCard, Meal
from .permissions import IsStaff
from .serializers import (
    AllocationSerializer, PeriodSerializer, AllocationDetailSerializer, 
    QRVerifySerializer, MealSerializer, UserSerializer, QRVerifyPostSerializer
)
from .utils.rebate_checker import is_student_on_rebate

# Constants
BREAKFAST_END_TIME = timezone.datetime.strptime('11:00:00', '%H:%M:%S').time()
LUNCH_END_TIME = timezone.datetime.strptime('15:00:00', '%H:%M:%S').time()

class LogoutView(APIView):
    """
    View to handle user logout.
    """
    permission_classes = [IsStaff]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)


class IsAuthenticated(APIView):
    """
    View to check if the user is authenticated.
    """
    permission_classes = [IsStaff]

    def get(self, request):
        if request.user.is_staff:
            return Response({"detail": "Authenticated"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class UserDetail(APIView):
    """
    View to get user details.
    """
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class AllocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing allocations.
    """
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
        return Allocation.objects.all()


class PeriodViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing periods.
    """
    permission_classes = [IsStaff]
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

    def get_queryset(self):
        return Period.objects.order_by('-start_date')[:1]


class QRVerifyView(generics.RetrieveAPIView):
    """
    View to verify QR codes.
    """
    permission_classes = [IsStaff]
    serializer_class = QRVerifySerializer
    queryset = MessCard.objects.all()
    lookup_field = 'id'


class QRVerifyUpdateView(APIView):
    """
    View to update QR verification.
    """
    permission_classes = [IsStaff]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_STRING, description='Card ID')
            },
            required=['id'],
        ),
        responses={
            200: 'Meal recorded successfully',
            400: 'Invalid card id or bad request',
            409: 'Meal already recorded.'
        }
    )
    def post(self, request):
        data = request.data
        serializer = QRVerifyPostSerializer(data={"id": data['id']})

        if serializer.is_valid():
            card_id = serializer.validated_data['id']
            try:
                card = MessCard.objects.get(id=card_id)
                card_return_data = QRVerifySerializer(card).data
                date = timezone.localtime().date()
                time = timezone.localtime().time()
                meal, _ = Meal.objects.get_or_create(mess_card=card, date=date)
                is_rebate = is_student_on_rebate(card.student, card.allocation)

                if card.allocation.caterer.name != request.user.username:
                    return Response({"success": False, "detail": "Wrong caterer.", "mess_card": card_return_data}, status=status.HTTP_403_FORBIDDEN)

                if is_rebate:
                    return Response({"success": False, "detail": "Student is on rebate.", "mess_card": card_return_data}, status=status.HTTP_403_FORBIDDEN)

                if time < BREAKFAST_END_TIME:
                    meal_type = 'breakfast'
                elif time < LUNCH_END_TIME:
                    meal_type = 'lunch'
                else:
                    meal_type = 'dinner'

                if getattr(meal, meal_type):
                    return Response({"success": False, "detail": "Meal Already Recorded", "mess_card": card_return_data}, status=status.HTTP_409_CONFLICT)

                setattr(meal, meal_type, True)
                meal.save()
                return Response({"success": True, "detail": "Meal recorded successfully", "mess_card": card_return_data}, status=status.HTTP_200_OK)
            except MessCard.DoesNotExist:
                return Response({"success": False, "detail": "Invalid card id."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing meals.
    """
    permission_classes = [IsStaff]
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
