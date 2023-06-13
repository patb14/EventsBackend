from django.db import models

from events.models.base_model import BaseModel


class Event(BaseModel):
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey("EventLocation", on_delete=models.DO_NOTHING)
    gender = models.ForeignKey("Gender", on_delete=models.DO_NOTHING)
    sessions = models.ManyToManyField("Session")
    cost = models.FloatField()

    def __str__(self):
        return f"{self.name}"
