from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


# Create your models here.
class Advertisement(models.Model):
    ad_id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        unique=True,
    )
    brand = models.CharField(max_length=100)
    flyer = models.ImageField(upload_to="ads")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")

    def __str__(self):
        return self.brand
