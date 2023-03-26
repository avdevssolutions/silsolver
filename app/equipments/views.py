from rest_framework import viewsets
from .models import Equipment, EquipmentForm
from .serializers import EquipmentSerializer, EquipmentDetailSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EmployeeDetailViewSet(viewsets.ModelViewSet):
    queryset = EquipmentForm.objects.all()
    serializer_class = EquipmentDetailSerializer
