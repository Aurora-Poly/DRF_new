from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
  path('signup/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('profile/<str:user__username>/', ProfileView.as_view(lookup_field = 'user__username')),

   # path('', include("rest_auth.urls")),
  #path('profile/', ProfileView.as_view()),
]