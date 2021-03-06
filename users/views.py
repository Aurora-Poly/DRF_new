from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Profile
from .permissions import CustomReadOnly
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer


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
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  #permission_classes = [IsAuthenticated, CustomReadOnly]


# class ProfileView(generics.GenericAPIView):
#   serializer_class = ProfileSerializer
#
#   def patch(self, request):
#     profile = Profile.objects.get(user=request.user)
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     data = serializer.validated_data
#     profile.univ = data['univ']
#     profile.dept = data['dept']
#     profile.age = data['age']
#     if request.data['image']:
#       profile.image = request.data['image']
#     profile.save()
#     return Response({"result": "ok"},
#                     status=status.HTTP_206_PARTIAL_CONTENT)
#
#   def get(self, request):
#     profile = Profile.objects.get(user=request.user)
#     serializer = self.get_serializer(profile)
#     return Response(serializer.data)
