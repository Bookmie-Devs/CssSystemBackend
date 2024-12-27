from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
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
    level = SerializerMethodField()

    class Meta:
        model = CustomUser
        exclude = (
            "is_staff",
            "password",
            "groups",
            "is_superuser",
            "user_permissions",
        )

    # get user level
    def get_level(self, obj: CustomUser):
        try:
            # levels should be in hundreds
            return f"{(int(obj.graduation_year) - int(timezone.now().year))*100}"
        except Exception:
            return "level unavailable, please check your graduation_year"
