from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from contest.models import Contest
from contest.permissions import IsOwnerOrReadOnly
from contest.serializer import ContestSerializer


class SetPagination(PageNumberPagination):
  page_size = 3
  page_query_param = 'page_size'
  max_page_size = 100
# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all().order_by('-id')
    serializer_class = ContestSerializer
    pagination_class = SetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #SearchFilter 기반 검색
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'profile__name','profile']
    search_fields = ['title']
