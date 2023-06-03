from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=64)
    start_time = models.TimeField()
    end_time = models.TimeField()
    occupancy_limit = models.IntegerField()
    current_occupancy = models.IntegerField(editable=False, default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
