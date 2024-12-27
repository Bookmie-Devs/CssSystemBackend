from django.contrib import admin
from acadamics.models import Course, OnlineTutorialTips, AcadamicSlides, PastQuestions

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_code", "course_name", "level", "created_at"]


@admin.register(OnlineTutorialTips)
class OnlineTutorialTipsAdmin(admin.ModelAdmin):
    list_display = ["course", "created_at", "approved"]


@admin.register(AcadamicSlides)
class AcadamicSlidesAdmin(admin.ModelAdmin):
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
                "fields": ("course",),
            },
        ),
        (
            "Slides",
            {
                "fields": ("file",),
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
                "fields": ("course",),
            },
        ),
        (
            "Pasco",
            {
                "fields": ("file",),
            },
        ),
    )
