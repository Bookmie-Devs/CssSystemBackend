from examination_system.models import ExaminationSchedule
from django.utils import timezone


class ExamScheduleRepository:
    model = ExaminationSchedule.objects

    @classmethod
    def get_exam_schedules(cls, level):
        # get all unwritten examnations and last 3 weeks written
        # any exam written before the weeks earlier wont be displayed
        return cls.model.filter(
            time__gt=(timezone.now() - timezone.timedelta(weeks=3)),
            course__level=int(level),
        ).all()
