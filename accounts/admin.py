from django.contrib import admin
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "phone",
        "is_active",
        "is_staff",
        "last_login",
    ]
    ordering = ["-last_login"]

    search_fields = ["first_name", "last_name", "phone", "email"]

    fieldsets = (
        ("Identity", {"fields": ("email",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        # (
        #     _("Validation"),
        #     {
        #         "fields": (
        #             "email_confirm",
        #             "phone_confirm",
        #         )
        #     },
        # ),
    )
