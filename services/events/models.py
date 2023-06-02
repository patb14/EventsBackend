from django.db import models

# TODO: DB VALS FOR ALL THESE MOFUCKAS
GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("C", "Co-ed")
]

YOB_CHOICE = [
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
]

LOP_CHOICES = [
    ("AAA", "AAA"),
    ("AA", "AA"),
    ("A", "A"),
]

POSITION_CHOICES = [
    ("FORWARD", "Forward"),
    ("DEFENSE", "Defense"),
    ("GOALIE", "Goalie")
]


class EventLocation(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField(max_length=128)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.address}"


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


class Event(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey(EventLocation, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=6,
                              choices=GENDER_CHOICES)
    times = models.ManyToManyField(EventTime)
    cost = models.FloatField()

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
