from django.db import models
from academics.models import Course
from uuid import uuid4
from django_google_maps import fields as map_fields

# Create your models here.


class ExaminationSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    index_number_start = models.CharField(default=0000, max_length=230)
    index_number_end = models.CharField(default=0000, max_length=230)
    time = models.DateTimeField(null=True)
    college = models.CharField(
        max_length=255,
        help_text="The college where the exam is suppose to take place",
    )
    room = models.CharField(max_length=230, null=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)
