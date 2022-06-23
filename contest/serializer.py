from rest_framework import serializers

from contest.models import Contest
from users.serializers import ProfileSerializer


class ContestSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Contest
    fields = ("pk", 'profile','title', 'tag', 'company', 'detail'
              ,'qualification','award','field','apply_url','img_url')

class ContestCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contest
    fields = ('title', 'tag', 'company', 'detail'
              ,'qualification','award','field','apply_url','img_url')