from rest_framework import generics, status, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from activity.models import Activity
from .models import Profile, ProfileImage
from .permissions import CustomReadOnly, IsOwner
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, ProfileImageSerializer, UserSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
    serializer = self.get_serializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data
    return Response({"token": token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
  model=Profile
  # queryset = Profile.objects.all()
  lookup_field = 'user__username'
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated, CustomReadOnly]
  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Profile.objects.filter(user=user).all()
    else:
      return Profile.objects.all()
    


class ProfileImageView(generics.ListCreateAPIView):
  model=Profile
  queryset = ProfileImage.objects.all()
  serializer_class = ProfileImageSerializer



class ProfileImageDetailView(generics.RetrieveUpdateDestroyAPIView):
  model=Profile
  queryset = ProfileImage.objects.all()
  lookup_field = 'user__username'
  serializer_class = ProfileImageSerializer




class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated, CustomReadOnly]
