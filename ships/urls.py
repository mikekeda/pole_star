from django.urls import path

from rest_framework import routers

from ships.views import homepage_view
from ships.viewsets import ShipsViewSet, PositionsViewSet

app_name = "Pole Star"

urlpatterns = [path("", homepage_view, name="maps")]

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"api/ships", ShipsViewSet, basename="Ship")
router.register(r"api/positions", PositionsViewSet, basename="ShipLocation")

urlpatterns += router.urls
