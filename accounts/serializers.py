from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from rest_framework import serializers
from accounts.models import (
    UserSavedPastQueations,
    PastQuestions,
    UserSavedBlogs,
    AcademicSlides,
    UserSavedSlides,
    UserSavedOnlineTutorialTips,
    OnlineTutorialTips,
    News,
)
from accounts.repository import (
    UserSavedPastQuestionsRepo,
    UserSavedBlogsRepo,
    UserSavedSlidesRepo,
    UserSavedOnlineTutorialTipsRepo,
)
from academics.serializers import (
    OnlineTutorialTipsSerializer,
    PastQuestionsSerializer,
    SlidesSerializer,
)
from news.serializers import NewsSerializer
from accounts.models import CustomUser
from django.contrib.auth.models import update_last_login
from typing import Dict, Any
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from accounts.models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField


class AccountSignupSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "index_number",
            "first_name",
            "last_name",
            "phone",
            "graduation_year",
            "password",
        )


class AccountProfileSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = (
            "is_staff",
            "password",
            "groups",
            "is_superuser",
            "user_permissions",
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = {
            "id": self.user.id,
            "index_number": self.user.index_number,
            "graduation_year": self.user.graduation_year,
            "level": self.user.get_level(),
            "phone": str(self.user.phone),
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "phone_confirm": self.user.phone_confirm,
        }

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


user_saved_blogs_repo = UserSavedBlogsRepo


class UserSavedBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSavedBlogs
        fields = ["id", "user", "blogs", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "created_at", "last_updated"]

    def create(self, validated_data: dict):
        user = self.context.get("request").user
        validated_data.update({"user": user})
        blogs_data = validated_data.pop("blogs", [])

        user_saved_blogs = user_saved_blogs_repo.get_user_saved_blogs(user=user)

        if user_saved_blogs:
            for blog in blogs_data:
                user_saved_blogs.blogs.add(blog)
            return user_saved_blogs

        user_saved_blog = user_saved_blogs_repo.create_user_saved_blogs(
            **validated_data
        )
        user_saved_blog.blogs.set(blogs_data)
        return user_saved_blog


class GetUserSavedBlogsSerializer(serializers.ModelSerializer):
    blogs = NewsSerializer(many=True)

    class Meta:
        model = UserSavedBlogs
        fields = ["id", "user", "blogs", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "blogs", "created_at", "last_updated"]


user_saved_slides_repo = UserSavedSlidesRepo


class UserSavedSlidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSavedSlides
        fields = ["id", "user", "slides", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "created_at", "last_updated"]

    def create(self, validated_data: dict):
        user = self.context.get("request").user
        validated_data.update({"user": user})
        slides_data = validated_data.pop("slides", [])

        user_saved_slides = user_saved_slides_repo.get_user_saved_slides(user=user)

        if user_saved_slides:
            for slide in slides_data:
                user_saved_slides.slides.add(slide)
            return user_saved_slides

        user_saved_slide = user_saved_slides_repo.create_user_saved_slides(
            **validated_data
        )
        user_saved_slide.slides.set(slides_data)
        return user_saved_slide


class GetUserSavedSlidesSerializer(serializers.ModelSerializer):
    slides = SlidesSerializer(many=True)

    class Meta:
        model = UserSavedSlides
        fields = ["id", "user", "slides", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "slides", "created_at", "last_updated"]


user_saved_tutorial_tips_repo = UserSavedOnlineTutorialTipsRepo


class UserSavedOnlineTutorialTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSavedOnlineTutorialTips
        fields = ["id", "user", "online_tips", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "created_at", "last_updated"]

    def create(self, validated_data: dict):
        user = self.context.get("request").user
        validated_data.update({"user": user})
        online_tips_data = validated_data.pop("online_tips", [])

        user_saved_tutorial_tips = (
            user_saved_tutorial_tips_repo.get_user_saved_tutorial_tips(user=user)
        )

        if user_saved_tutorial_tips:
            for online_tip in online_tips_data:
                user_saved_tutorial_tips.online_tips.add(online_tip)
            return user_saved_tutorial_tips

        user_saved_tutorial_tip = (
            user_saved_tutorial_tips_repo.create_user_saved_tutorial_tips(
                **validated_data
            )
        )
        user_saved_tutorial_tip.online_tips.set(online_tips_data)
        return user_saved_tutorial_tip


class GetUserSavedOnlineTutorialTipsSerializer(serializers.ModelSerializer):
    online_tips = serializers.PrimaryKeyRelatedField(
        queryset=OnlineTutorialTips.objects.all(), many=True
    )

    class Meta:
        model = UserSavedOnlineTutorialTips
        fields = ["id", "user", "online_tips", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "online_tips", "created_at", "last_updated"]


user_saved_past_questions_repo = UserSavedPastQuestionsRepo


class UserSavedPastQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSavedPastQueations
        fields = ["id", "user", "past_questions", "created_at", "last_updated"]
        read_only_fields = ["id", "user", "created_at", "last_updated"]

    def create(self, validated_data: dict):
        user = self.context.get("request").user
        validated_data.update({"user": user})
        past_questions_data = validated_data.pop("past_questions", [])

        user_saved_past_questions = (
            user_saved_past_questions_repo.get_user_saved_past_questions(user=user)
        )

        if user_saved_past_questions:
            for past_question in past_questions_data:
                user_saved_past_questions.past_questions.add(past_question)
            return user_saved_past_questions

        user_saved_past_question = (
            user_saved_past_questions_repo.create_user_saved_past_questions(
                **validated_data
            )
        )
        user_saved_past_question.past_questions.set(past_questions_data)
        return user_saved_past_question


class GetUserSavedPastQuestionsSerializer(serializers.ModelSerializer):
    past_questions = serializers.PrimaryKeyRelatedField(
        queryset=PastQuestions.objects.all(), many=True
    )

    class Meta:
        model = UserSavedPastQueations
        fields = ["id", "user", "past_questions", "created_at", "last_updated"]
        read_only_fields = [
            "id",
            "user",
            "past_questions",
            "created_at",
            "last_updated",
        ]
