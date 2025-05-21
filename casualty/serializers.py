from rest_framework import serializers
from .models import Patient
from bson import ObjectId
# Custom field to handle ObjectId
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return str(data)
class PatientSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)  # :point_left: Add this line to use custom field
    class Meta:
        model = Patient
        fields = '__all__'


# serializers.py

from rest_framework import serializers
from .models import PatientRegister

class PatientRegisterSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = PatientRegister
        fields = '__all__'




# serializers.py
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
