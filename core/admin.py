from django.contrib import admin
from core.models import NotifyUser, ContactUs

# Register your models here.


class NotifyUserAdmin(admin.ModelAdmin):
    list_display = [
        "recipient",
        "action",
        "created_at",
        "last_updated",
    ]


class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "created_at",
    ]

    list_filter = ["created_at"]


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(NotifyUser, NotifyUserAdmin)
