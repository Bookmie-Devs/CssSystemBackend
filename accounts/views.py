from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, GenericAPIView, CreateAPIView
from accounts.repository import UserRepository
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
    GetUserSavedBlogsSerializer,
)
from accounts.services import (
    register_service,
    user_profile_service,
    get_user_saved_blogs,
    delete_saved_blog,
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
