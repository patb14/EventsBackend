from django.db import models

from events.models.base_model import BaseModel


class Gender(BaseModel):
    gender = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.gender}"
