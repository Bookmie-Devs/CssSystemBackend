from django.contrib import admin
from advertisements.models import Advertisement

# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["brand", "flyer", "created_at"]
