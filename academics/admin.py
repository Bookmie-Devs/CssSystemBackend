from django.contrib import admin
from academics.models import (
    Course,
    OnlineTutorialTips,
    AcademicSlides,
    PastQuestions,
    InternshipOpportunities,
)
from django.utils import timezone

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_code", "course_name", "level", "created_at"]


@admin.register(OnlineTutorialTips)
class OnlineTutorialTipsAdmin(admin.ModelAdmin):
    list_display = ["course", "created_at", "approved"]


@admin.register(InternshipOpportunities)
class InternshipOpportunitiesAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = (
        "campany_name",
        "application_deadline",
        "created_at",
        "get_application_status",
    )

    # Add filtering options in the list view
    list_filter = ("application_deadline", "created_at")

    # Allow searching by company name and description
    search_fields = ("campany_name", "description")

    # Sort the list by application deadline by default
    ordering = ("-application_deadline",)

    # Add a method to show the application status (if deadline is passed)
    def get_application_status(self, obj):
        if obj.application_deadline and obj.application_deadline < timezone.now():
            return "Expired"
        return "Active"

    get_application_status.short_description = "Application Status"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "campany_name",
                    "description",
                    "registration_link",
                    "image",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("application_deadline",),
                "classes": ("collapse",),
            },
        ),
    )

    actions = ["mark_as_expired"]

    def mark_as_expired(self, request, queryset):
        updated_count = queryset.update(application_deadline=timezone.now())
        self.message_user(request, f"{updated_count} internship(s) marked as expired.")

    mark_as_expired.short_description = "Mark selected internships as expired"


@admin.register(AcademicSlides)
class AcademicSlidesAdmin(admin.ModelAdmin):
    list_display = [
        "course",
        "file",
        "created_at",
        "approved",
    ]
    fieldsets = (
        (
            "Course",
            {
                "fields": (
                    "course",
                    "title",
                ),
            },
        ),
        (
            "Slides",
            {
                "fields": (
                    "file",
                    "approved",
                ),
            },
        ),
    )


@admin.register(PastQuestions)
class PastQuestionsAdmin(admin.ModelAdmin):
    list_display = [
        "course",
        "file",
        "created_at",
        "approved",
    ]
    fieldsets = (
        (
            "Course",
            {
                "fields": (
                    "course",
                    "title",
                ),
            },
        ),
        (
            "Pasco",
            {
                "fields": (
                    "file",
                    "approved",
                ),
            },
        ),
    )
