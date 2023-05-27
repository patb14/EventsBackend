from datetime import datetime

from django.db import models


class UserAccount(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.CharField(max_length=64)
    creation_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
