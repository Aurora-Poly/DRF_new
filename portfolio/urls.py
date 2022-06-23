from django.urls import path
from rest_framework import routers

from portfolio.views import PortfolioViewSet

router = routers.SimpleRouter()
router.register('portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns= router.urls