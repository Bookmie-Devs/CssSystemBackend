from utils.utils import notify_user
from django.db import models
from accounts.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
action = [("send", "send"), ("draft", "draft")]


class NotifyUser(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField(help_text="Message for the user")
    created_at = models.DateTimeField(auto_now_add=True)
    action = models.CharField(choices=action, default="draft", max_length=255)
    sent = models.BooleanField(default=False, editable=False)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.action.lower() == "sent":
            notify_user(self.recipient.phone, self.message)
            self.action = "send"
            self.sent = True
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "notify_user"
        verbose_name = "Notify User"
        verbose_name_plural = "Notify User"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(null=True)
    message = models.TextField()
    created_at = models.DateTimeField(verbose_name="Sent on", auto_now_add=True)

    class Meta:
        verbose_name = "Reported Issue"
        verbose_name_plural = "Reported Issues"
