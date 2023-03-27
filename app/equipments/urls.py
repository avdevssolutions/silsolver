from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'equipments', views.EquipmentViewSet)
router.register(r'equipment-details', views.EquipmentDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
