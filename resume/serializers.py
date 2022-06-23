from rest_framework import serializers

from resume.models import Resume
from users.serializers import ProfileSerializer


class ResumeSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)

  class Meta:
    model = Resume
    fields = ("pk", 'profile', 'title', 'file_upload', 'date', 'comments')

class ResumeCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Resume
    fields = ('title', 'file_upload', 'date', 'comments')