from django.contrib import admin
from executives.models import Executive, ExecutivePosition, ExecutiveSocialLinks
# Register your models here.


@admin.register(ExecutivePosition)
class ExecutivePositionAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "last_updated"]

@admin.register(ExecutiveSocialLinks)
class ExecutiveSocialLinksAdmin(admin.ModelAdmin):
    list_display = ["executive", "platform"]


@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    def official_name(self, obj):
        return f"Mr. {obj.user.first_name} {obj.user.last_name}"

    list_display = ["official_name", "position", "is_active", "office_from"]
