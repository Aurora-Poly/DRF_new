from rest_framework.routers import DefaultRouter
from .views import VolunteerViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('volunteer', VolunteerViewSet)

urlpatterns = [
  path('', include(router.urls)),
]