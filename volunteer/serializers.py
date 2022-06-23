from rest_framework import serializers

from .models import Volunteer
from users.serializers import ProfileSerializer


class VolunteerSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Volunteer
    fields = ("pk", 'profile', 'title', 'company', 'detail',
              'location', 'applyperiod', 'actperiod')

class VolunteerCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    fields = ('title', 'company', 'detail',
              'location', 'applyperiod', 'actperiod')