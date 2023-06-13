from django.db import models

from events.models.base_model import BaseModel


class PlayerPosition(BaseModel):
    position = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.position}"
