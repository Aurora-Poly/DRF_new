from django.urls import path
from rest_framework import routers

from activity import views
from activity.views import ActivityViewSet, like_post, like_list, LikeListView, RecommendView

router = routers.SimpleRouter()
router.register('activity', ActivityViewSet)


urlpatterns = router.urls +[
  path('activity/like/<int:pk>/', like_post, name='like_post'),
  path('likelist/', LikeListView.as_view()),
  path('recommend/', RecommendView.as_view()),

]
