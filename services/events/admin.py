from django.contrib import admin

from .models import Event, EventTime, EventLocation

admin.site.register(Event)
admin.site.register(EventTime)
admin.site.register(EventLocation)
