from django.db import models

from events.models.base_model import BaseModel


class EventLocation(BaseModel):
    name = models.CharField(max_length=64)
    address = models.TextField(max_length=128)

    def __str__(self):
        return f"{self.name} - {self.address}"
