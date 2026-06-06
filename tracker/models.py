from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class VehicleCount(models.Model):

    VEHICLES = (
        ('BUS','BUS'),
        ('COSTER','COSTER'),
        ('TAXI','TAXI'),
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLES
    )

    count = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.user} {self.vehicle_type}"