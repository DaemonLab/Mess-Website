from rest_framework import serializers
from home.models import Allocation, Period, Student, Caterer
from qrscan.models import MessCard, Meal

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
        fields = ['id', 'allocation', 'student', 'qr_code', 'secret_key']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'mess_card', 'date', 'breakfast', 'lunch', 'dinner']
