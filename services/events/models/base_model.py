import uuid

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True)
