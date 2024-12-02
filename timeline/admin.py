from django.contrib import admin
from timeline.models import Timeline
from django.utils.html import format_html

# Register your models here.


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    def timeline(self, obj):
        return format_html(
            '<a href={}><img src="{}" width="50" height="50" /></a>',
            obj.image.url,
            obj.image.url,
        )

    list_display = ["event", "timeline", "created_at"]
