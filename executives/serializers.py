from rest_framework import serializers
from .models import ExecutivePosition, Executive, ExecutiveSocialLinks


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



class ExecutiveSocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveSocialLinks
        fields = ['id', 'executive', 'platform']
#
# class ExecutiveProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExecutiveProfile
#         fields = ["image"]
#


class ExecutiveSerializer(serializers.ModelSerializer):
    position = ExecutivePositionSerializer()
    executive_name = serializers.SerializerMethodField()
    social_media_links = ExecutiveSocialLinksSerializer(many=True)

    class Meta:
        model = Executive
        fields = [
            "executive_name",
            "executive_id",
            "position",
            "image",
            "social_media_links",
            "office_from",
            "is_active",
        ]

    def get_executive_name(self, obj: Executive):
        return f"{obj.user.first_name} {obj.user.last_name}"
