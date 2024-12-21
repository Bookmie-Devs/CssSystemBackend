from examination_system.models import ExaminationSchedule
from django.utils import timezone


class ExamScheduleRepository:
    model = ExaminationSchedule.objects

    @classmethod
    def get_exam_schedules(cls):
        return cls.model.filter(time__gt=timezone.now()).all()
