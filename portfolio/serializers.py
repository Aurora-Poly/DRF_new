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
  # image = serializers.SerializerMethodField()
  # files = serializers.SerializerMethodField()

  # def get_files(self, obj):
  #   file = obj.file.all()
  #   return PostFileSerializer(instance=file, many=True, context=self.context).data

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
  image = PostImageSerializer()
  file = PostFileSerializer()

  # def get_files(self, obj):
  #   file = obj.file.all()
  #   return PostFileSerializer(instance=file, many=True, context=self.context).data

  class Meta:
    model = Portfolio
    fields = ('title', 'category', 'content', 'date' , 'image', 'file')

  # head_img= Base64ImageField(
  #       max_length=None, use_url=True,
  #   )
# class Base64ImageField(serializers.ImageField):
#   """
#   A Django REST framework field for handling image-uploads through raw post data.
#   It uses base64 for encoding and decoding the contents of the file.
#
#   Heavily based on
#   https://github.com/tomchristie/django-rest-framework/pull/1268
#
#   Updated for Django REST framework 3.
#   """
#
#   def to_internal_value(self, data):
#     from django.core.files.base import ContentFile
#     import base64
#     import six
#     import uuid
#
#     # Check if this is a base64 string
#     if isinstance(data, six.string_types):
#       # Check if the base64 string is in the "data:" format
#       if 'data:' in data and ';base64,' in data:
#         # Break out the header from the base64 content
#         header, data = data.split(';base64,')
#
#       # Try to decode the file. Return validation error if it fails.
#       try:
#         decoded_file = base64.b64decode(data)
#       except TypeError:
#         self.fail('invalid_image')
#
#       # Generate file name:
#       file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
#       # Get the file name extension:
#       file_extension = self.get_file_extension(file_name, decoded_file)
#
#       complete_file_vname = "%s.%s" % (file_name, file_extension,)
#
#       data = ContentFile(decoded_file, name=complete_file_name)
#
#     return super(Base64ImageField, self).to_internal_value(data)
#
#   def get_file_extension(self, file_name, decoded_file):
#     import imghdr
#
#     extension = imghdr.what(file_name, decoded_file)
#     extension = "jpg" if extension == "jpeg" else extension
#
#     return extension