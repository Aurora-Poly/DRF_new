from rest_framework import serializers

from activity.models import Activity
from users.serializers import ProfileSerializer


class ActivitySerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Activity
    fields = ("pk", 'profile','title', 'tag', 'company', 'apply_period', 'field'
              ,'field', 'actperiod', 'personnel', 'detail', 'apply_url'
              , 'img_url', 'likes')

class ActivityCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = ('title', 'tag', 'company', 'apply_period', 'field'
              ,'field', 'actperiod', 'personnel', 'detail', 'apply_url'
              , 'img_url')