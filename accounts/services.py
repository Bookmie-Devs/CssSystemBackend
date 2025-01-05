from accounts.repository import UserRepository
from rest_framework import status
from examination_system.repositories import ExamScheduleRepository
from accounts.repository import (
    UserSavedBlogsRepo,
    UserSavedOnlineTutorialTipsRepo,
    UserSavedPastQuestionsRepo,
    UserSavedSlidesRepo,
)
from academics.repository import (
    OnlineTutorialTipsRepository,
    SlidesRepository,
    PastQuestionsRepository,
)
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


def remove_saved_online_tip(request, pk):
    ok = status.HTTP_200_OK
    bad = status.HTTP_400_BAD_REQUEST
    not_found = status.HTTP_404_NOT_FOUND
    user = request.user
    online_tip = OnlineTutorialTipsRepository.get_online_tip(pk=pk)
    if online_tip is None:
        return not_found, {
            "status": "error",
            "message": "No blogs exists",
        }
    saved_tips = UserSavedOnlineTutorialTipsRepo.get_user_saved_tutorial_tips(user=user)
    saved_tips.links.remove(online_tip)

    context = {
        "status": "Success",
        "message": "Online tip deleted",
    }
    return ok, context


def remove_saved_slide(request, pk):
    ok = status.HTTP_200_OK
    bad = status.HTTP_400_BAD_REQUEST
    not_found = status.HTTP_404_NOT_FOUND
    user = request.user
    slide = SlidesRepository.get_slide(pk=pk)
    if slide is None:
        return not_found, {
            "status": "error",
            "message": "No slide found with this ID",
        }
    saved_slides = UserSavedSlidesRepo.get_user_saved_slides(user=user)
    saved_slides.slides.remove(slide)

    context = {
        "status": "success",
        "message": "Slide deleted from saved slides",
    }
    return ok, context


def remove_saved_past_question(request, pk):
    ok = status.HTTP_200_OK
    bad = status.HTTP_400_BAD_REQUEST
    not_found = status.HTTP_404_NOT_FOUND
    user = request.user
    past_question = PastQuestionsRepository.get_past_question(pk=pk)
    if past_question is None:
        return not_found, {
            "status": "error",
            "message": "No past question found with this ID",
        }
    saved_past_questions = UserSavedPastQuestionsRepo.get_user_saved_past_questions(
        user=user
    )
    saved_past_questions.past_questions.remove(past_question)

    context = {
        "status": "success",
        "message": "Past question deleted from saved questions",
    }
    return ok, context


def get_user_saved_academic_resources(
    request,
    slides_serializer_class,
    online_tips_serializer,
    past_questions_serializer,
):
    ok = status.HTTP_200_OK
    user = request.user
    slides = UserSavedSlidesRepo.get_user_saved_slides(user=user)
    online_tips = UserSavedOnlineTutorialTipsRepo.get_user_saved_tutorial_tips(
        user=user
    )
    past_questions = UserSavedPastQuestionsRepo.get_user_saved_past_questions(user=user)
    context = {
        "status": "success",
        "message": "user saved resources",
        "data": {
            "slides": slides_serializer_class(slides).data,
            "past_questions": past_questions_serializer(past_questions).data,
            "online_tutorial_tips": online_tips_serializer(online_tips).data,
        },
    }
    return ok, context
