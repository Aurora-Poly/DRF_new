from django.urls import path
from rest_framework import routers

from resume.views import ResumeViewSet, ResumeFileViewSet

router = routers.SimpleRouter()
router.register('resume', ResumeViewSet, basename='resume')
router.register('resumefile',  ResumeFileViewSet, basename='resumefile')
urlpatterns= router.urls