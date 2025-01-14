from django.contrib import admin
from news.models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["reported_by", "title", "created_at"]
    fieldsets = (
        (
            "Meta Data",
            {
                "fields": ("reported_by",),
            },
        ),
        (
            "Content",
            {
                "fields": (
                    "title",
                    "report",
                    "minutes_read",
                ),
            },
        ),
        (
            "Media",
            {
                "fields": (
                    "head_image",
                    "back_image",
                )
            },
        ),
    )
