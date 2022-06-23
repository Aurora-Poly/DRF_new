from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from resume.models import Resume
from resume.permissions import IsOwner
from resume.serializers import ResumeSerializer, ResumeCreateSerializer
from users.models import Profile

class SetPagination(PageNumberPagination):
  page_size = 8
  page_query_param = 'page_size'
  max_page_size = 100

class ResumeViewSet(viewsets.ModelViewSet):
  filter_backends = [SearchFilter]
  search_fields = ['title']
  pagination_class = SetPagination
  permission_classes = [IsAuthenticated, IsOwner]
  # queryset = Resume.objects.all()
  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Resume.objects.filter(user=user).order_by('-pk')
    else:
      return Resume.objects.none()


  def get_serializer_class(self):
    if self.action == 'list' or 'retrieve':
      return ResumeSerializer
    return ResumeCreateSerializer

  def perform_create(self, serializer):
    profile = Profile.objects.get(user=self.request.user)
    serializer.save(user=self.request.user, profile=profile)

# class PortfolioList(generics.ListAPIView):
#   serializers_class = PortfolioSerializer
#   def get_queryset(self):
#     user = self.request.user
#     if user.is_authenticated:
#       return Portfolio.objects.filter(portfolio=user)
#     else:
#       return Portfolio.objects.none()


