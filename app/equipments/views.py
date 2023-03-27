from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Equipment, EquipmentForm
from .serializers import EquipmentSerializer, EquipmentDetailSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all().order_by('pk')
    serializer_class = EquipmentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Object successfully deleted."},
                        status=status.HTTP_200_OK)


class EquipmentDetailViewSet(viewsets.ModelViewSet):
    queryset = EquipmentForm.objects.all().order_by('pk')
    serializer_class = EquipmentDetailSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Object successfully deleted."},
                        status=status.HTTP_200_OK)
