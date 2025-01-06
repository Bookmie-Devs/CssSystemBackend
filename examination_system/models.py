from django.db import models
from academics.models import Course
from uuid import uuid4
from django_google_maps import fields as map_fields
from accounts.repository import UserRepository
from utils.utils import send_examination_schedule_message
from django.utils import timezone

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
    message_schedule = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The time a message is suppose to be sent all students who have this exam; If no time is set the system will send message 1 hour before the paper",
    )
    geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # fetch students within level and index number range
        students = UserRepository.fetch_examination_students_phone(
            level=self.course.level,
            index_number_start=self.index_number_start,
            index_number_end=self.index_number_end,
        )
        print(students)
        if students:
            # only run when we have students in the list and list is not empty
            msg_scheduled_at = (
                self.message_schedule
                if self.message_schedule
                else (self.time - timezone.timedelta(hours=2))
            ).strftime("%Y-%m-%d %H:%M")
            context = {
                "exam_date": self.time.date(),
                "exam_time": self.time.time(),
                "course": self.course.course_name,
                "college": self.college,
                "room": self.room,
            }
            print(msg_scheduled_at)
            send_examination_schedule_message(students, msg_scheduled_at, context)
        return super().save(*args, **kwargs)
