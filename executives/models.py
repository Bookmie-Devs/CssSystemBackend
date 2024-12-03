from django.db import models
from accounts.models import CustomUser
from uuid import uuid4

# Create your models here.


class ExecutivePosition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return str(self.name)


class Executive(models.Model):
    executive_id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        unique=True,
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.ForeignKey(ExecutivePosition, on_delete=models.CASCADE)
    office_from = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Mr. {self.user.first_name} {self.user.last_name}"


class ExecutiveProfile(models.Model):
    executive = models.ForeignKey(
        Executive,
        on_delete=models.CASCADE,
        related_name="profiles",
    )
    image = models.ImageField(upload_to="profile_images", null=True)
