from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from accounts.repository import UserRepository
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from examination_system.serializers import ExaminationScheduleSerializer
from rest_framework.request import Request
from accounts.serializers import AccountSignupSerializer, AccountProfileSerializer
from accounts.services import register_service, user_profile_service


class RegisterView(GenericAPIView):
    serializer_class = AccountSignupSerializer

    def post(self, request: Request):
        service = register_service
        status, context = service(request, self.serializer_class)
        return Response(status=status, data=context)


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
