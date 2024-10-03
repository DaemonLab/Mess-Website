from rest_framework import viewsets, generics
from home.models import Allocation, Period
from qrscan.models import MessCard, Meal
from .serializers import AllocationSerializer, PeriodSerializer, AllocationDetailSerializer, QRVerifySerializer, MealSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the token for the user
            token = Token.objects.get(user=request.user)
            # Delete the token to log out the user
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        

class IsAuthenticated(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            return Response({"detail": "Authenticated"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AllocationViewSet(viewsets.ReadOnlyModelViewSet):    
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
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

    def get_queryset(self):
        return Period.objects.order_by('-start_date')[:1]
    

class QRVerifyView(generics.RetrieveAPIView):
    serializer_class = QRVerifySerializer
    queryset = MessCard.objects.all()
    lookup_field = 'id'


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
