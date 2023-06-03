from django.db import models


class LevelOfPlay(models.Model):
    level_of_play = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.level_of_play}"
