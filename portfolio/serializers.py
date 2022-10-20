import null as null
from rest_framework import serializers

from portfolio.models import Portfolio, PostImage, PostFile
from users.serializers import ProfileSerializer

class PostImageSerializer(serializers.ModelSerializer):
  # image = serializers.ImageField(use_url=True)
  class Meta:
    model = PostImage
    fields = ('image', 'post')
    lookup_field = 'post__pk'

    extra_kwargs = {
      'url': {'lookup_field': 'post'}
    }

class PostFileSerializer(serializers.ModelSerializer):
  file = serializers.FileField(use_url=True)

  class Meta:
    model = PostFile
    fields = ['file', 'post']

class PortfolioSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  image = PostImageSerializer(read_only=True)
  file = PostFileSerializer(read_only=True)

  class Meta:
    model = Portfolio
    fields = ("pk", 'profile', 'title', 'content','date', 'image', 'file' )

  def create(self, validated_data):
    instance = Portfolio.objects.create(**validated_data)
    file_set = self.context['request'].FILES
    image_set = self.context['request'].FILES

    for image_data in image_set.getlist('image'):
      PostImage.objects.create(post=instance, image=image_data)
    for file_data in file_set.getlist('file'):
      PostFile.objects.create(post=instance, file=file_data)
    return instance




class PortfolioCreateSerializer(serializers.ModelSerializer):
  image = PostImageSerializer(read_only=True)
  file = PostFileSerializer(read_only=True)

  class Meta:
    model = Portfolio
    fields = ('title', 'content', 'date' , 'image', 'file')

  def create(self, validated_data):
    instance = Portfolio.objects.create(**validated_data)
    file_set = self.context['request'].FILES
    image_set = self.context['request'].FILES

    for image_data in image_set.getlist('image'):
      PostImage.objects.create(post=instance, image=null)
    for file_data in file_set.getlist('file'):
      PostFile.objects.create(post=instance, file=file_data)
    return instance
