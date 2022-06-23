from rest_framework import serializers

from club.models import Club
from users.serializers import ProfileSerializer


class ClubSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  class Meta:
    model = Club
    fields = ("pk", 'profile','title', 'personnel', 'content', 'date')

class ClubCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Club

    fields = ('title', 'personnel', 'content', 'date')