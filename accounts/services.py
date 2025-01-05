from accounts.repository import UserRepository
from rest_framework import status
from examination_system.repositories import ExamScheduleRepository
from accounts.repository import UserSavedBlogsRepo
from news.repository import NewsRepository


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
        graduation_year = serializer.validated_data["graduation_year"]

        repo.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            index_number=index_number,
            password=password,
            graduation_year=graduation_year,
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
    exams = serializer_classes["exams"](
        exams_repo.get_exam_schedules(level=user.get_level()), many=True
    )
    context = {"user": serializer.data, "exams": exams.data}
    return (ok, context)


def get_user_saved_blogs(request, serializer_class, *args, **kwargs):
    ok = status.HTTP_200_OK
    user = request.user
    saved_blogs = UserSavedBlogsRepo.get_user_saved_blogs(user=user)
    serializer = serializer_class(saved_blogs)
    return ok, {
        "status": "success",
        "message": "user saved blogs",
        "data": serializer.data,
    }


def delete_saved_blog(request, news_blog_id):
    ok = status.HTTP_200_OK
    bad = status.HTTP_400_BAD_REQUEST
    not_found = status.HTTP_404_NOT_FOUND
    user = request.user
    news_blog = NewsRepository.get_news_blog(news_id=news_blog_id)
    if news_blog is None:
        return not_found, {
            "status": "error",
            "message": "No blogs exists",
        }
    saved_blogs = UserSavedBlogsRepo.get_user_saved_blogs(user=user)
    saved_blogs.blogs.remove(news_blog)

    context = {
        "status": "Success",
        "message": "Blog deleted from",
    }
    return ok, context
