from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from examination_system.models import ExaminationSchedule


# Register your models here.
class ExaminationScheduleAdmin(admin.ModelAdmin):
    list_filter = [
        "course",
        "college",
        "room",
    ]
    formfield_overrides = {
        map_fields.AddressField: {"widget": map_widgets.GoogleMapsAddressWidget},
    }
    fieldsets = (
        (
            "Examination Schedule",
            {
                "fields": (
                    "course",
                    "college",
                    "room",
                    "time",
                    "index_number_start",
                    "index_number_end",
                ),
            },
        ),
        (
            "Map",
            {
                "fields": (
                    "address",
                    "geolocation",
                ),
            },
        ),
    )


admin.site.register(ExaminationSchedule, ExaminationScheduleAdmin)
