from django.db import models

LOCATION_CHOICES = [
    ("KRC", "KRC"),
    ("CARDELL", "Cardell"),
    ("SENSPLEX", "Sensplex")
]

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


class Event(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=32,
                                choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=6,
                              choices=GENDER_CHOICES)
    times = models.CharField(max_length=256)
    cost = models.CharField(max_length=64)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"