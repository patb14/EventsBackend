from django.db import models

from events.models.base_model import BaseModel


class Session(BaseModel):
    name = models.CharField(max_length=64)
    start_time = models.TimeField()
    end_time = models.TimeField()
    occupancy_limit = models.IntegerField()
    current_occupancy = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.name

    def public_label(self):
        return self.start_time
