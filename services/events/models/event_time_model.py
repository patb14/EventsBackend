from django.db import models


class EventTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.start_time > self.end_time:
            raise ValueError("End Time must be after Start Time")

        super().save(force_insert, force_update, using, update_fields)
