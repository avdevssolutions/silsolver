from rest_framework import serializers
from .models import Equipment, EquipmentForm

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentForm
        fields = '__all__'
