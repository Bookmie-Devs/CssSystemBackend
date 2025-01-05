from accounts.models import CustomUser
from .models import (
    UserSavedBlogs,
    UserSavedSlides,
    UserSavedOnlineTutorialTips,
    UserSavedPastQueations,
)


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
