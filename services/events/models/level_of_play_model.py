from django.db import models

from events.models.base_model import BaseModel


class LevelOfPlay(BaseModel):
    level_of_play = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.level_of_play}"
