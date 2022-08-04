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

from portfolio.models import Portfolio
from users.models import Profile
from .permissions import IsOwner
from .serializers import PortfolioSerializer, PortfolioCreateSerializer

class SetPagination(PageNumberPagination):
  page_size = 8
  page_query_param = 'page_size'
  max_page_size = 100
class PortfolioViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated, IsOwner]
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['title']
  pagination_class = SetPagination

  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Portfolio.objects.filter(user=user).order_by('-id')
    else:
      return Portfolio.objects.none()

  def get_serializer_class(self):
    if self.action == 'list' or 'retrieve':
      return PortfolioSerializer
    return PortfolioCreateSerializer

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


