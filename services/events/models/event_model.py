from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey("EventLocation", on_delete=models.DO_NOTHING)
    gender = models.ForeignKey("Gender", on_delete=models.DO_NOTHING)
    # TODO: This will have to change to One to Many since event times will have an occupancy limit
    #       Probably smart to just make a Session model. An Event can have multiple sessions and those sessions can only
    #       be associated with this event. A session has an occupancy limit, time range, etc. In short times -> sessions
    times = models.ManyToManyField("EventTime")
    cost = models.FloatField()

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
