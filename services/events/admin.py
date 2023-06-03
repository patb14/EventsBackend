from django.contrib import admin

from .models import Event, EventLocation, Gender, LevelOfPlay, PlayerPosition, EventTime

admin.site.register(Event)
admin.site.register(EventTime)
admin.site.register(EventLocation)
admin.site.register(Gender)
admin.site.register(LevelOfPlay)
admin.site.register(PlayerPosition)
