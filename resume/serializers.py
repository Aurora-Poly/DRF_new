from rest_framework import serializers

from resume.models import Resume, ResumeFile
from users.serializers import ProfileSerializer

class ResumeFileSerializer(serializers.ModelSerializer):
  file = serializers.FileField(use_url=True)

  class Meta:
    model = ResumeFile
    fields = ['file', 'post']

class ResumeSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  resume_file = ResumeFileSerializer(read_only=True)

  class Meta:
    model = Resume
    fields = ("pk", 'profile', 'title',  'date', 'comments', 'resume_file')


  def create(self, validated_data):
    instance = Resume.objects.create(**validated_data)
    file_set = self.context['request'].FILES

    for file_data in file_set.getlist('file'):
      ResumeFile.objects.create(post=instance, file=file_data)
    return instance

class ResumeCreateSerializer(serializers.ModelSerializer):
  resume_file = ResumeFileSerializer(read_only=True)
  class Meta:
    model = Resume
    fields = ('title', 'date', 'comments', 'resume_file')

  def create(self, validated_data):
    instance = Resume.objects.create(**validated_data)
    file_set = self.context['request'].FILES

    for file_data in file_set.getlist('file'):
      ResumeFile.objects.create(post=instance, file=file_data)
    return instance

