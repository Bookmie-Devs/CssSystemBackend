from django.db import models
from uuid import uuid4


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    decription = models.TextField()
    event_image_1 = models.ImageField(upload_to="event_images", null=True)
    event_image_2 = models.ImageField(upload_to="event_images", null=True)
    event_date = models.DateTimeField(null=True, blank=False)
    organised_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.event_name

    class Meta:
        ordering = ["-created_at"]
