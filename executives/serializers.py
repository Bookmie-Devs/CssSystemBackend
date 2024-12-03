from rest_framework import serializers
from .models import ExecutivePosition, Executive, ExecutiveProfile
from accounts.models import CustomUser


class ExecutivePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutivePosition
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "last_updated",
        ]


class ExecutiveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveProfile
        fields = ["image"]


class ExecutiveSerializer(serializers.ModelSerializer):
    position = ExecutivePositionSerializer()
    profiles = ExecutiveProfileSerializer(many=True)

    class Meta:
        model = Executive
        fields = [
            "executive_id",
            "user",
            "profiles",
            "position",
            "office_from",
            "is_active",
        ]
