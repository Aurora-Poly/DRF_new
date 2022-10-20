from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from activity.models import Activity
from activity.permissions import CustomReadOnly
from activity.reml import find_sim_num
from activity.serializers import ActivitySerializer, ActivityCreateSerializer, LikeListSerializer, ActivityRecSerializer
from users.models import Profile

class SetPagination(PageNumberPagination):
  page_size = 10
  page_query_param = 'page_size'
  max_page_size = 100

class ActivityViewSet(viewsets.ModelViewSet):
  queryset = Activity.objects.all().order_by('-id')
  permission_classes = [CustomReadOnly]
  pagination_class = SetPagination
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['field', 'target', 'prize', 'office', 'likes']
  search_fields = ['title']

  def get_serializer_class(self):
    if self.action == 'list' or 'retrieve':
      return ActivitySerializer
    return ActivityCreateSerializer

  def perform_create(self, serializer):
    profile = Profile.objects.get(user=self.request.user)
    serializer.save(author=self.request.user, profile=profile)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
  activity = get_object_or_404(Activity, pk=pk)
  if request.user in activity.likes.all():
    activity.likes.remove(request.user)
  else:
    activity.likes.add(request.user)

  return Response({'status': 'ok'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_list(request, pk):
  pagination_class = SetPagination
  my = get_object_or_404(User, pk=pk)
  lookup_field = 'user__username'
  data=[]
  for activity in Activity.objects.filter(likes=request.user).order_by('-id'):
    serializer = ActivitySerializer(activity)
    data.append(serializer.data)

class LikeListView(generics.ListAPIView):
  serializer_class = ActivitySerializer
  # lookup_field = 'user__username'
  pagination_class = SetPagination
  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Activity.objects.filter(likes=user)
    else:
      return Activity.objects.none()


class RecommendView(generics.ListAPIView):
  serializer_class = ActivitySerializer
  # pagination_class = SetPagination
  def get_queryset(self):
    user = self.request.user
    data = []
    if user.is_authenticated:
      for activity in Activity.objects.filter(likes=user).order_by():

        raw_recos = find_sim_num(activity.id)
        recommendation_dict = raw_recos
        data.insert(0, recommendation_dict)
        print("activity: ",activity.id," data: ",recommendation_dict)
      print('data:' ,data[:3])
      return Activity.objects.filter(id__in=data[:3]).order_by()
      # return Activity.objects.filter(id__in=["1", "2", "3"])
    else:
      return Activity.objects.filter(id__in=["3","2","5"])



