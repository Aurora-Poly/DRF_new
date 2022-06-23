from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contest.views import ContestViewSet

router = DefaultRouter()
router.register('contest', ContestViewSet)

urlpatterns = [
  path('', include(router.urls)),
]