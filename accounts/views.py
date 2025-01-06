from rest_framework.generics import DestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
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
    PhoneVericationSerializer,
    ChangePasswordSerializer,
    ResetPasswordSerializer,
    RequestPhoneVerificationSerializer,
    RequestForgotPasswordSerializer,
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
    request_password_reset_service,
    phone_verification_service,
    reset_password_service,
    request_phone_verification_service,
    delete_your_account_service,
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


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        service = delete_your_account_service
        status, context = service(request)
        return Response(status=status, data=context)


class RequestPhoneNumberVerificationView(CreateAPIView):
    serializer_class = RequestPhoneVerificationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        service = request_phone_verification_service
        status, context = service(request, self.serializer_class)
        return Response(status=status, data=context)


class PhoneVerifcationView(CreateAPIView):
    serializer_class = PhoneVericationSerializer

    def post(self, request, *args, **kwargs):
        service = phone_verification_service
        status, context = service(request, self.serializer_class)
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


# for forgot password
class RequestForgotPasswordResetView(CreateAPIView):
    serializer_class = RequestForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        service = request_password_reset_service
        status, context = service(request, self.serializer_class)
        return Response(data=context, status=status)


# for forgot password
class ResetPasswordView(CreateAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        service = reset_password_service
        status, context = service(request, self.serializer_class)
        return Response(data=context, status=status)


# """
#     this should not be confuse with reset password where the user does
#     not need to be authenticated and is assume to have forgotten
#     his/her password
#  """
class ChangePasswordView(CreateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_password = serializer.validated_data.get("new_password")
            user = request.user
            user.set_password(new_password)
            user.save()
            return Response(
                data={
                    "status": "success",
                    "message": "Password Change was successfull",
                },
                status=status.HTTP_200_OK,
            )
        return super().post(request, *args, **kwargs)


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
