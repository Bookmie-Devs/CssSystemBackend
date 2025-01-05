from django.contrib import admin
from core.models import NotifyUser

# Register your models here.


class NotifyUserAdmin(admin.ModelAdmin):
    list_display = [
        "recipient",
        "action",
        "created_at",
        "last_updated",
    ]


admin.site.register(NotifyUser, NotifyUserAdmin)
