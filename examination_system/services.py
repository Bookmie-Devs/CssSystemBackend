from examination_system.repositories import ExamScheduleRepository
from rest_framework import status


def get_exam_schedules_service(request, serializer_classes):
    ok = status.HTTP_200_OK
    exams_repo = ExamScheduleRepository
    # bad = status.HTTP_400_BAD_REQUEST
    user = request.user
    exams = serializer_classes["exams"](
        exams_repo.get_exam_schedules(level=user.get_level()), many=True
    )
    context = exams.data
    return (ok, context)
