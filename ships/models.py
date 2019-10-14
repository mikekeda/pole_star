from django.db import models
from django.contrib.gis.db.models import PointField


class Ship(models.Model):
    """ Ship location model. """

    imo = models.IntegerField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ShipLocation(models.Model):
    """ Ship location model. """

    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = PointField()
