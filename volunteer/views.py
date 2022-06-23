from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from volunteer.models import Volunteer
from volunteer.serializers import VolunteerSerializer


class SetPagination(PageNumberPagination):
  page_size = 8
  page_query_param = 'page_size'
  max_page_size = 100

class VolunteerViewSet(viewsets.ModelViewSet):
  queryset = Volunteer.objects.all().order_by('-id')
  serializer_class = VolunteerSerializer
  pagination_class = SetPagination
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['title', 'profile__name', 'profile']
  search_fields = ['title']

  # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
      serializer.save(author=self.request.user)
