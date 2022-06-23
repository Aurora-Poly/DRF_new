from django.urls import path
from rest_framework import routers

from resume.views import ResumeViewSet

router = routers.SimpleRouter()
router.register('resume', ResumeViewSet, basename='resume')

urlpatterns= router.urls