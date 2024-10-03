from rest_framework import serializers
from home.adapters.account_adapter import User
from home.models import Allocation, Period, Student, Caterer
from qrscan.models import MessCard, Meal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_staff', 'is_superuser', 'username', 'last_login', 'date_joined', "first_name", "last_name"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'email', 'name']

class CatererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterer
        fields = ['id', 'name']

class AllocationSerializer(serializers.ModelSerializer):
    caterer = CatererSerializer()

    class Meta:
        model = Allocation
        fields = ['id', 'student_id', 'email', 'caterer']

class AllocationDetailSerializer(serializers.ModelSerializer):
    email = StudentSerializer()
    caterer = CatererSerializer()

    class Meta:
        model = Allocation
        fields = ['id', 'period_id', 'student_id', 'email', 'caterer', 'email']

class PeriodSerializer(serializers.ModelSerializer):
    allocation_set = AllocationSerializer(many=True, read_only=True)

    class Meta:
        model = Period
        fields = '__all__'

class QRVerifySerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    allocation = AllocationSerializer()
    class Meta:
        model = MessCard
        fields = ['id', 'allocation', 'student', 'qr_code']


class QRVerifyPostSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'mess_card', 'date', 'breakfast', 'lunch', 'dinner']
