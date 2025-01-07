from django.db import models
from uuid import uuid4

# Create your models here.


# this model handles both blogs and news though the name suggest otherwise
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
    minutes_read = models.IntegerField(default=0)
    head_image = models.ImageField(upload_to="news", null=True)
    back_image = models.ImageField(upload_to="news", null=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    last_updted = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    class Meta:
        db_table = "news_blogs"
        verbose_name = "News/Blogs"
        verbose_name_plural = "News/Blogs"
