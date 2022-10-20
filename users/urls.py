from django.urls import path, include
from rest_framework import routers

from .views import RegisterView, LoginView, ProfileView, ProfileImageView, ProfileImageDetailView, UserViewSet

router = routers.DefaultRouter()
router.register('info', UserViewSet)




urlpatterns = [
  path('', include(router.urls)),
  path('signup/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('profile/<str:user__username>/', ProfileView.as_view(lookup_field = 'user__username')),
  path('profileimg/', ProfileImageView.as_view()),
  path('profileimg/<str:user__username>/', ProfileImageDetailView.as_view(lookup_field = 'user__username')),
]