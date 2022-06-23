from django.urls import path
from rest_framework import routers

from activity.views import ActivityViewSet, like_post

router = routers.SimpleRouter()
router.register('activity', ActivityViewSet)

urlpatterns = router.urls +[
  path('activity/like/<int:pk>/', like_post, name='like_post'),
]
