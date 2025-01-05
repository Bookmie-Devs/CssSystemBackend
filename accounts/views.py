from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, GenericAPIView, CreateAPIView

from accounts.repository import UserRepository
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase
from examination_system.serializers import ExaminationScheduleSerializer
from rest_framework.request import Request
from accounts.serializers import (
    AccountSignupSerializer,
    AccountProfileSerializer,
    CustomTokenObtainPairSerializer,
    UserSavedBlogsSerializer,
    UserSavedOnlineTutorialTips,
    UserSavedSlidesSerializer,
    UserSavedPastQueations,
    UserSavedPastQuestionsSerializer,
    UserSavedOnlineTutorialTipsSerializer,
    GetUserSavedBlogsSerializer,
    GetUserSavedPastQuestionsSerializer,
    GetUserSavedOnlineTutorialTipsSerializer,
    GetUserSavedSlidesSerializer,
)
from accounts.services import (
    register_service,
    user_profile_service,
    get_user_saved_blogs,
    delete_saved_blog,
    remove_saved_online_tip,
    get_user_saved_academic_resources,
    remove_saved_slide,
    remove_saved_past_question,
)


class RegisterView(GenericAPIView):
    serializer_class = AccountSignupSerializer

    def post(self, request: Request):
        service = register_service
        status, context = service(request, self.serializer_class)
        return Response(status=status, data=context)


class LoginView(TokenViewBase):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_classes = {
        "user": AccountProfileSerializer,
        "exams": ExaminationScheduleSerializer,
    }

    def get(self, request: Request):
        service = user_profile_service
        status, context = service(request, self.serializer_classes)
        return Response(status=status, data=context)


class SaveBlogView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSavedBlogsSerializer


class GetUserSavedBlogs(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSavedBlogsSerializer

    def get(self, request):
        service = get_user_saved_blogs
        status, context = service(request, self.serializer_class)
        return Response(status=status, data=context)


class RemoveSavedBlogView(DestroyAPIView):
    """
    Removind saved blog
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, news_blog_id):
        service = delete_saved_blog
        status, context = service(request, news_blog_id=news_blog_id)
        return Response(status=status, data=context)


class SaveOnlineTipResourceView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSavedOnlineTutorialTipsSerializer


class SaveSlideResourceView(CreateAPIView):
    """
    Save slide for the user
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSavedSlidesSerializer


class SavePastQuestionResourceView(CreateAPIView):
    """
    Save past question for the user
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSavedPastQuestionsSerializer


class RemoveSavedOnlineResourceTipsView(APIView):
    """
    Removing saved online tutorial tips
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, online_tip_id):
        service = remove_saved_online_tip
        status, context = service(request, pk=online_tip_id)
        return Response(status=status, data=context)


class RemoveSavedSlidesView(APIView):
    """
    Removing saved slides
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, slide_id):
        service = remove_saved_slide
        status, context = service(request, pk=slide_id)
        return Response(status=status, data=context)


class RemoveSavedPastQuestionsView(APIView):
    """
    Removing saved past questions
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, past_question_id):
        service = remove_saved_past_question
        status, context = service(request, pk=past_question_id)
        return Response(status=status, data=context)


class GetUserSavedAcademicResources(GenericAPIView):
    permission_classes = [IsAuthenticated]
    # ser = serializer
    online_tips_ser = GetUserSavedOnlineTutorialTipsSerializer
    slides_ser = GetUserSavedSlidesSerializer
    past_question_ser = GetUserSavedPastQuestionsSerializer

    def get(self, request, *args, **kwargs):
        service = get_user_saved_academic_resources
        status, context = service(
            request=request,
            slides_serializer_class=self.slides_ser,
            online_tips_serializer=self.online_tips_ser,
            past_questions_serializer=self.past_question_ser,
        )
        return Response(status=status, data=context)
