from django.db import models
from accounts.models import CustomUser
from uuid import uuid4

# Create your models here.


class News(models.Model):
    news_id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4,
        editable=False,
    )
    title = models.CharField(max_length=100)
    reported_by = models.CharField(max_length=100)
    report = models.TextField()
    head_image = models.ImageField(upload_to="news", null=True, blank=True)
    back_image = models.ImageField(upload_to="news", null=True, blank=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    last_updted = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    class Meta:
        verbose_name_plural = "News"
