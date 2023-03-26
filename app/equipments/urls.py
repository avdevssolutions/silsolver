from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'equipments', views.EmployeeViewSet)
router.register(r'equipment-details', views.EmployeeDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
