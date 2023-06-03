from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.gender}"
