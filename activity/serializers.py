from rest_framework import serializers

from activity.models import Activity
from users.serializers import ProfileSerializer


class ActivitySerializer(serializers.ModelSerializer):
  # profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Activity
    fields = '__all__'

class ActivityCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = '__all__'