from accounts.models import CustomUser
from .models import (
    UserSavedBlogs,
    UserSavedSlides,
    UserSavedOnlineTutorialTips,
    UserSavedPastQueations,
    PhoneVerifcationCodes,
)
from django.utils import timezone
from django.db.models import ExpressionWrapper, F, IntegerField
from django.contrib.auth.hashers import make_password


class UserRepository:
    model = CustomUser.objects

    @classmethod
    def create_user(
        cls,
        phone,
        first_name,
        last_name,
        index_number,
        graduation_year,
        password,
    ):
        try:
            user = cls.model.create_user(
                first_name=first_name,
                last_name=last_name,
                index_number=index_number,
                graduation_year=graduation_year,
                phone=phone,
                password=password,
            )
            return user
        except CustomUser.DoesNotExist:
            return None

    @classmethod
    def get_user_by_phone(cls, phone):
        return cls.model.filter(phone=phone).first()

    @classmethod
    def check_if_staff(cls, index_number):
        try:
            cls.model.get(
                index_number=index_number,
                is_active=True,
                is_staff=True,
            )
            return True
        except Exception:
            return False

    @classmethod
    def get_users_by_level(cls, target_level):
        current_year = timezone.now().year
        return cls.model.annotate(
            level=ExpressionWrapper(
                (4 - (F("graduation_year") - current_year)) * 100,
                output_field=IntegerField(),
            )
        ).filter(level=target_level)

    @classmethod
    def fetch_examination_students_phone(cls, level):
        # this is to fetch all students and send them message for exam starts
        phones = [
            f"0{str(user.phone).removeprefix('+233')}"
            for user in cls.get_users_by_level(target_level=level)
        ]
        return phones


class PhoneVerificationCodeRepo:
    model = PhoneVerifcationCodes.objects

    @classmethod
    def create_code(cls, phone, code):
        _code = make_password(code)
        if cls.model.filter(phone=phone).exists():
            cls.model.get(phone=phone).delete()
        cls.model.create(phone=phone, code=_code)

    @classmethod
    def check_code(cls, phone):
        try:
            v_code = cls.model.get(phone=phone)
            return True, v_code
        except:
            return False, None


class UserSavedBlogsRepo:
    not_found = UserSavedBlogs.DoesNotExist
    model = UserSavedBlogs.objects

    @classmethod
    def get_user_saved_blogs(cls, user):
        try:
            blogs = cls.model.get(user=user)
        except cls.not_found:
            return None
        else:
            return blogs

    @classmethod
    def create_user_saved_blogs(cls, **kwargs):
        saved_blog = cls.model.create(**kwargs)
        return saved_blog


class UserSavedSlidesRepo:
    not_found = UserSavedSlides.DoesNotExist
    model = UserSavedSlides.objects

    @classmethod
    def get_user_saved_slides(cls, user):
        try:
            slides = cls.model.get(user=user)
        except cls.not_found:
            return None
        else:
            return slides

    @classmethod
    def create_user_saved_slides(cls, **kwargs):
        saved_slide = cls.model.create(**kwargs)
        return saved_slide


class UserSavedOnlineTutorialTipsRepo:
    not_found = UserSavedOnlineTutorialTips.DoesNotExist
    model = UserSavedOnlineTutorialTips.objects

    @classmethod
    def get_user_saved_tutorial_tips(cls, user):
        try:
            tutorial_tips = cls.model.get(user=user)
        except cls.not_found:
            return None
        else:
            return tutorial_tips

    @classmethod
    def create_user_saved_tutorial_tips(cls, **kwargs):
        saved_tips = cls.model.create(**kwargs)
        return saved_tips


class UserSavedPastQuestionsRepo:
    not_found = UserSavedPastQueations.DoesNotExist
    model = UserSavedPastQueations.objects

    @classmethod
    def get_user_saved_past_questions(cls, user):
        try:
            past_questions = cls.model.get(user=user)
        except cls.not_found:
            return None
        else:
            return past_questions

    @classmethod
    def create_user_saved_past_questions(cls, **kwargs):
        saved_past_questions = cls.model.create(**kwargs)
        return saved_past_questions
