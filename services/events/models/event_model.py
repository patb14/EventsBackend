from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey("EventLocation", on_delete=models.DO_NOTHING)
    gender = models.ForeignKey("Gender", on_delete=models.DO_NOTHING)
    sessions = models.ManyToManyField("Session")
    cost = models.FloatField()

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
