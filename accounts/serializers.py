from rest_framework.serializers import Serializer, ModelSerializer, CharField
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
