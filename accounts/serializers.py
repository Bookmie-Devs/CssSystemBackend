from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
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
