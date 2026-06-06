from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=200)

    event_date = models.DateField()

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name