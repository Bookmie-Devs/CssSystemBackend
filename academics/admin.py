from django.contrib import admin
from academics.models import Course, OnlineTutorialTips, AcademicSlides, PastQuestions

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_code", "course_name", "level", "created_at"]


@admin.register(OnlineTutorialTips)
class OnlineTutorialTipsAdmin(admin.ModelAdmin):
    list_display = ["course", "created_at", "approved"]


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
                "fields": ("course", "description",),
            },
        ),
        (
            "Slides",
            {
                "fields": ("file", "approved",),
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
                "fields": ("course", "description",),
            },
        ),
        (
            "Pasco",
            {
                "fields": ("file", "approved",), 
            },
        ),
    )
