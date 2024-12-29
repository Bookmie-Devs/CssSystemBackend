from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.

type_of_resource = [
    ("slides", "slides"),
    ("video", "video"),
    ("audio", "audio"),
    ("file", "file"),
]


class Course(models.Model):
    course_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    course_name = models.CharField(max_length=200, null=True, blank=False)
    course_code = models.CharField(max_length=200, unique=True)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return str(f"{self.course_name} level {self.level}")


class OnlineTutorialTips(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="online_tips",
    )
    link = models.URLField(("resource_link"), max_length=200)
    type_of_resource = models.CharField(choices=type_of_resource, max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    approved = models.BooleanField(default=False)

    class Meta:
        # verbose_name = _("")
        verbose_name_plural = _("Online Tutorial Tips")

    def __str__(self) -> str:
        return f"{self.course.course_name} Online Tip"


class AcademicSlides(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="slides")
    file = models.FileField(_("Sildes"), upload_to="slides", max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    approved = models.BooleanField(default=False)

    class Meta:
        # verbose_name = _("")
        # db_table = "academics slides"
        verbose_name_plural = _("Academic Slides")

    def __str__(self) -> str:
        return f"{self.course.course_name} Slide"



class PastQuestions(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="past_questions"
    )
    file = models.FileField(_("Sildes"), upload_to="slides", max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    approved = models.BooleanField(default=False)

    class Meta:
        # verbose_name = _("")
        verbose_name_plural = _("Past Questions")

    def __str__(self) -> str:
        return f"{self.course.course_name} Past Questions"
