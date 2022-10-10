from django.urls import path
from rest_framework import routers

from activity import views
from activity.views import ActivityViewSet, like_post, like_list, recommend

router = routers.SimpleRouter()
router.register('activity', ActivityViewSet)


urlpatterns = router.urls +[
  path('activity/like/<int:pk>/', like_post, name='like_post'),
  path('<int:pk>/like_list/',like_list, name='like_list'),
  #  path('profile/<str:user__username>/', ProfileView.as_view(lookup_field = 'user__username')),
  # path('activity/like_list/', like_list, name='like_list'),
  # path('<int:pk>/like/', like_list, name='like_list')
  path('recommend/<int:pk>/', recommend,  name='recommend'),
]
