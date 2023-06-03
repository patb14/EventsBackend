from django.db import models


class EventLocation(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField(max_length=128)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.address}"
