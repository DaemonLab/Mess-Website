from rest_framework import serializers
from home.adapters.account_adapter import User
from home.models import Allocation, Period, Student, Caterer
from qrscan.models import MessCard, Meal

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    class Meta:
        model = User
        fields = ['id', 'email', 'is_staff', 'is_superuser', 'username', 'last_login', 'date_joined', 'first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model."""
    class Meta:
        model = Student
        fields = ['id', 'email', 'name']


class CatererSerializer(serializers.ModelSerializer):
    """Serializer for Caterer model."""
    class Meta:
        model = Caterer
        fields = ['id', 'name']


class AllocationSerializer(serializers.ModelSerializer):
    """Serializer for Allocation model."""
    caterer = CatererSerializer(read_only=True)

    class Meta:
        model = Allocation
        fields = ['id', 'student_id', 'email', 'caterer']


class AllocationDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Allocation model."""
    student = StudentSerializer(read_only=True)
    caterer = CatererSerializer(read_only=True)

    class Meta:
        model = Allocation
        fields = ['id', 'period_id', 'student_id', 'student', 'caterer']


class PeriodSerializer(serializers.ModelSerializer):
    """Serializer for Period model."""
    allocation_set = AllocationSerializer(many=True, read_only=True)

    class Meta:
        model = Period
        fields = '__all__'


class QRVerifySerializer(serializers.ModelSerializer):
    """Serializer for QR verification."""
    student = StudentSerializer(read_only=True)
    allocation = AllocationSerializer(read_only=True)

    class Meta:
        model = MessCard
        fields = ['id', 'allocation', 'student', 'qr_code']


class QRVerifyPostSerializer(serializers.Serializer):
    """Serializer for QR verification POST request."""
    id = serializers.UUIDField(required=True)


class MealSerializer(serializers.ModelSerializer):
    """Serializer for Meal model."""
    class Meta:
        model = Meal
        fields = ['id', 'mess_card', 'date', 'breakfast', 'lunch', 'dinner']
