from django.db import models


class PlayerPosition(models.Model):
    position = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.position}"
