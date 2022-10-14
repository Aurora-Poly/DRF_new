from rest_framework import serializers

from activity.models import Activity


class ActivitySerializer(serializers.ModelSerializer):
  # profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Activity
    fields = '__all__'
class ActivityRecSerializer(serializers.ModelSerializer):
  # profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Activity
    # fields = ['id', 'title', 'juchae', 'jukwan', 'apply_period',
    #             'prize_1st', 'apply_url', 'image_url']
    fields = ['id']
class ActivityCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = '__all__'

class LikeListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = ['id', 'likes']
    extra_kwargs = {
      'url': {'lookup_field': 'user__username'}
    }