from rest_framework import serializers
from .models import ExecutivePosition, Executive


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


#
# class ExecutiveProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExecutiveProfile
#         fields = ["image"]
#


class ExecutiveSerializer(serializers.ModelSerializer):
    position = ExecutivePositionSerializer()
    executive_name = serializers.SerializerMethodField()

    class Meta:
        model = Executive
        fields = [
            "executive_name",
            "executive_id",
            "position",
            "image",
            "office_from",
            "is_active",
        ]

    def get_executive_name(self, obj: Executive):
        return f"{obj.user.first_name} {obj.user.last_name}"
