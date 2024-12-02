from django.contrib import admin
from events.models import Event
from django.utils.html import format_html

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ["-event_date"]

    def _event_flyer(self, obj):
        return format_html(
            '<a href={}><img src="{}" width="50" height="50" /></a>',
            obj.event_flyer.url,
            obj.event_flyer.url,
        )

    list_display = ["event_name", "_event_flyer", "organised_by", "event_date"]
