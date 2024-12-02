from django.db import models
from events.models import Event
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.


class Timeline(models.Model):
    timeline_id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4,
        editable=False,
    )
    event = models.ForeignKey(
        Event,
        verbose_name=_("Event"),
        on_delete=models.CASCADE,
        related_name="timeline",
    )
    image = models.ImageField(upload_to="timeline", null=True)
    decription = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.event.event_name} Timeline"
