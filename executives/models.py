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
    image = models.ImageField(upload_to="profile_images", null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.ForeignKey(ExecutivePosition, on_delete=models.CASCADE)
    office_from = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Mr. {self.user.first_name} {self.user.last_name}"




platform_choices = [
    ("facebook", "Facebook"),
    ("twitter", "Twitter"),
    ("instagram", "Instagram"),
    ("linkedin", "LinkedIn"),
    ("youtube", "YouTube"),
    ("snapchat", "Snapchat"),
    ("tiktok", "TikTok"),
    ("pinterest", "Pinterest"),
    ("reddit", "Reddit"),
    ("whatsapp", "WhatsApp"),
    ("telegram", "Telegram"),
    ("discord", "Discord"),
    ("twitch", "Twitch"),
    ("flickr", "Flickr"),
    ("quora", "Quora"),
    ("medium", "Medium"),
    ("github", "GitHub"),
    ("slack", "Slack"),
]

class ExecutiveSocialLinks(models.Model):
    executive = models.ForeignKey(
        Executive,
        on_delete=models.CASCADE,
        related_name="social_media_links",
    )
    platform = models.CharField(max_length=255, choices=platform_choices)
    link = models.URLField()

    class Meta:
        db_table= "executives_social_links"
        verbose_name = "Executive social links"
        verbose_name_plural = "Executive social links"

