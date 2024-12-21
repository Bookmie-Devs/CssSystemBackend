from accounts.repository import UserRepository
from rest_framework import status
from examination_system.repositories import ExamScheduleRepository


def register_service(request, serializer_class):
    ok = status.HTTP_200_OK
    repo = UserRepository
    serializer = serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        phone = serializer.validated_data["phone"]
        index_number = serializer.validated_data["index_number"]
        first_name = serializer.validated_data["first_name"]
        last_name = serializer.validated_data["last_name"]
        password = serializer.validated_data["password"]
        repo.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            index_number=index_number,
            password=password,
        )
        context = {
            "status": "success",
            "detail": "user registration complete",
            "data": None,
        }
        return (ok, context)


def user_profile_service(request, serializer_classes):
    ok = status.HTTP_200_OK
    exams_repo = ExamScheduleRepository
    # bad = status.HTTP_400_BAD_REQUEST
    user = request.user
    serializer = serializer_classes["user"](user)
    # exams = serializer_classes["exams"](exams_repo.get_exam_schedules())
    context = {"user": serializer.data,}
    return (ok, context)
