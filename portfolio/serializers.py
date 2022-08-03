from rest_framework import serializers

from portfolio.models import Portfolio
from users.serializers import ProfileSerializer


class PortfolioSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)

  class Meta:
    model = Portfolio
    fields = ("pk", 'profile', 'title', 'content', 'head_img', 'file_upload' ,'date')

class PortfolioCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portfolio
    fields = ('title', 'category', 'content', 'head_img', 'file_upload' , 'date')