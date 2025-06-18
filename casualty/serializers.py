from rest_framework import serializers
from .models import ERPatient
from bson import ObjectId
# Custom field to handle ObjectId
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return str(data)
    #ER form
class PatientSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)  # :point_left: Add this line to use custom field
    class Meta:
        model = ERPatient
        fields = '__all__'


# serializers.py

from rest_framework import serializers
from .models import ERPatientRegister

class PatientRegisterSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = ERPatientRegister
        fields = '__all__'







