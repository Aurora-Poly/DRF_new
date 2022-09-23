from rest_framework import serializers

from .models import Volunteer
from users.serializers import ProfileSerializer


class VolunteerSerializer(serializers.ModelSerializer):
  # profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Volunteer
    fields = '__all__'

class VolunteerCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    fields = '__all__'