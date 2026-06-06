from django.contrib import admin

from accounts.models import Profile
from events.models import Event
from tracker.models import VehicleCount

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(VehicleCount)