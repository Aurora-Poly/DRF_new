from rest_framework.routers import DefaultRouter
from .views import ClubViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('club', ClubViewSet)

urlpatterns = [
  path('', include(router.urls)),
]