from rest_framework import viewsets, serializers
from rest_framework.response import Response

from ships.models import Ship, ShipLocation


# Serializers.
class ShipSerializer(serializers.Serializer):
    """ Ship Serializer. """

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    imo = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


# ViewSets.
class ShipsViewSet(viewsets.ReadOnlyModelViewSet):
    """ Ship ViewSet. """

    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class PositionsViewSet(viewsets.ReadOnlyModelViewSet):
    """ ShipLocations ViewSet. """

    def retrieve(self, request, pk=None, *args, **kwargs):
        locations = ShipLocation.objects.filter(ship__imo=pk).order_by("-timestamp")
        return Response(
            [
                {
                    "latitude": obj.location.x,
                    "longitude": obj.location.y,
                    "timestamp": obj.timestamp,
                }
                for obj in locations
            ]
        )
