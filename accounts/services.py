from accounts.repository import UserRepository
from rest_framework import status
from rest_framework.request import Request
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from examination_system.repositories import ExamScheduleRepository
from accounts.repository import (
    UserSavedBlogsRepo,
    UserSavedOnlineTutorialTipsRepo,
    UserSavedPastQuestionsRepo,
    UserSavedSlidesRepo,
    PhoneVerificationCodeRepo,
)
from utils.utils import send_sms_message, normalize_phone, generate_code
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


def request_phone_verification_service(request, serializer_class):
    """
    A Service for requesting any phone verification that will be later verified
    """
    serializer = serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # phone = serializer.validated_data["phone"] # generate a interation error
        _phone = request.data.get("phone")
        # normalize phone number to able to send sms with mnotify
        phone = normalize_phone(_phone)
        code = generate_code(max=5)
        PhoneVerificationCodeRepo.create_code(phone=_phone, code=code)
        send_sms_message(
            phone=phone,
            template="phone_verification.txt",
            context={
                "code": code,
                "fname": request.user.first_name,
            },
        )
        context = {
            "status": "success",
            "message": f"Verification code sent to {phone}.",
            "data": serializer.data,
        }
        return status.HTTP_200_OK, context


def phone_verification_service(request, serializer_class):
    """
    Service for verifying code sent to a students phone
    """
    serializer = serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        phone = request.data.get("phone")
        code = request.data.get("code")
        exists, v_code = PhoneVerificationCodeRepo.check_code(phone=phone)
        if exists and check_password(code, v_code.code):
            if timezone.now() >= v_code.expires_in:
                context = {
                    "status": "failure",
                    "message": "Sms has expired.",
                    "data": {"phone": phone},
                }
                v_code.delete()
                return status.HTTP_400_BAD_REQUEST, context
            context = {
                "status": "success",
                "message": "Phone number verified.",
                "data": {"phone": phone},
            }
            v_code.delete()
            try:
                # for if the user has not completed signup yet or phone does not exists
                user = UserRepository.get_user_by_phone(phone=phone)
                user.phone_confirm = True
                user.save()
            except:
                pass
            return status.HTTP_200_OK, context
        else:
            context = {
                "status": "failure",
                "message": "Phone number verification failed.",
                "data": {"phone": phone},
            }


def request_password_reset_service(request: Request, serializer_class):
    bad = status.HTTP_400_BAD_REQUEST
    ok = status.HTTP_200_OK
    repo = PhoneVerificationCodeRepo
    user_repo = UserRepository
    serializer = serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # phone = serializer.validated_data["phone"] # generate a interation error
        _phone = request.data.get("phone")
        user = user_repo.get_user_by_phone(phone=_phone)
        if not user:
            context = {
                "status": "failed",
                "message": f"No user with phone {_phone}.",
                "data": None,
            }
            return (bad, context)
        # normalize phone number to able to send sms with mnotify
        phone = normalize_phone(_phone)
        code = generate_code(max=5, reset_password=True)
        repo.create_code(phone=_phone, code=code)
        send_sms_message(
            phone=phone,
            template="reset_password.txt",
            context={"code": code, "fname": user.first_name},
        )
        context = {
            "status": "success",
            "message": f"Password reset code sent to {phone}.",
            "data": None,
        }
        return (ok, context)


def reset_password_service(request, serailizer_class):
    ok = status.HTTP_200_OK
    repo = PhoneVerificationCodeRepo
    bad = status.HTTP_400_BAD_REQUEST
    user_repo = UserRepository
    serailizer = serailizer_class(data=request.data)
    if serailizer.is_valid(raise_exception=True):
        phone = request.data.get("phone")
        code = request.data.get("code")
        new_password = request.data.get("new_password")
        exists, v_code = repo.check_code(phone=phone)
        if exists and check_password(code, v_code.code):
            if timezone.now() >= v_code.expires_in:
                context = {
                    "status": "failure",
                    "message": "Sms has expired.",
                    "data": {"phone": phone},
                }
                v_code.delete()
                return bad, context
            context = {
                "status": "success",
                "message": "Password reset was successfull.",
                "data": {"phone": phone},
            }
            v_code.delete()
            try:
                # for if the user has not completed signup yet or phone does not exists
                user = user_repo.get_user_by_phone(phone=phone)
                user.set_password(new_password)
                user.save()
            except:
                pass
            return ok, context
        else:
            context = {
                "status": "failure",
                "message": "Code verification failed.",
                "data": {"phone": phone},
            }
            return bad, context


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
    saved_tips.online_tips.remove(online_tip)

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


def delete_your_account_service(request):
    ok = status.HTTP_200_OK
    user_id = request.user.pk
    UserRepository.delete_account(user_id)
    context = {
        "status": "success",
        "message": "Your account has been deleted",
    }
    return ok, context
