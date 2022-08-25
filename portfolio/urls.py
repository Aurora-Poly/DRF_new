from django.urls import path
from rest_framework import routers

from portfolio.views import PortfolioViewSet, ImageViewSet, FileViewSet

router = routers.SimpleRouter()
router.register('portfolio', PortfolioViewSet, basename='portfolio')
router.register('postimage',  ImageViewSet, basename='postImage')
router.register('postfile',  FileViewSet, basename='postFile')
urlpatterns= router.urls