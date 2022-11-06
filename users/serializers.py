from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, generics
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from activity.serializers import ActivitySerializer
from users.models import Profile, ProfileImage


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required = True,
    validators = [UniqueValidator(queryset = User.objects.all())],
  )

  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password],
  )

  password2 = serializers.CharField(write_only=True, required= True)

  class Meta:
    model = User
    fields = ('username', 'password', 'password2', 'email')

  def validate(self, data):
    if data['password'] != data['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."}
      )
    return data

  def create(self, validate_data):
    user = User.objects.create_user(
      #username = validate_data['username'],
      username=validate_data['username'],
      email=validate_data['email']
    )

    user.set_password(validate_data['password'])
    user.save()
    token = Token.objects.create(user=user)
    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(required=True)
  password = serializers.CharField(required=True, write_only=True)

  def validate(self,data):
    user = authenticate(**data)
    if user:
      token = Token.objects.get(user=user)
      return token
    raise serializers.ValidationError(
      {"error": "Unable to log in with provided credentials"}
    )


class ProfileImageSerializer(serializers.ModelSerializer):
  # image = serializers.ImageField(use_url=True)
  class Meta:
    model = ProfileImage
    fields = ('image', 'user')
    lookup_field = 'user__username'

    extra_kwargs = {
      'url': {'lookup_field': 'user'}
    }

class ProfileSerializer(serializers.ModelSerializer):
  image = ProfileImageSerializer(read_only=True)

  class Meta:

    model = Profile
    fields = ['user','univ', 'dept', 'age', 'image']
    lookup_field = 'user__username'

    extra_kwargs = {
      'url': {'lookup_field': 'user'}
    }

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  class Meta:
    model = User()
    fields = ['id', 'username','email', 'profile']

#아이디 중복 검사
class UsernameUniqueCheckSerializer(serializers.ModelSerializer):
  user = serializers.CharField(required=True, min_length=3, max_length=30,
  validators=[UniqueValidator(queryset=Profile.objects.all())])

  class Meta:
    model = User
    fields = ['username','user']