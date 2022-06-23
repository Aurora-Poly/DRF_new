from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from club.models import Club
from club.permissions import IsOwnerOrReadOnly
from club.serializers import ClubSerializer

class SetPagination(PageNumberPagination):
  page_size = 8
  page_query_param = 'page_size'
  max_page_size = 100

class ClubViewSet(viewsets.ModelViewSet):
  queryset = Club.objects.all().order_by('-id')
  serializer_class = ClubSerializer
  pagination_class = SetPagination
  filter_backends=[DjangoFilterBackend, SearchFilter]
  filterset_fields=['title','profile__name']
  search_fields = ['title']
 #permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
