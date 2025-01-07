from news.models import News
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class NewsSerializer(ModelSerializer):
    head_image_url = SerializerMethodField()
    back_image_url = SerializerMethodField()

    class Meta:
        model = News
        fields = [
            "news_id",
            "title",
            "reported_by",
            "report",
            "minutes_read",
            "head_image_url",
            "back_image_url",
            "views",
            "created_at",
            "last_updted",
        ]
        # Optionally, you can add read_only_fields for fields you do not want users to update
        read_only_fields = ["news_id", "created_at", "last_updted"]

    def get_head_image_url(self, obj):
        # This method will return the absolute URL for head_image if it's not null
        # used to get relative path beacause the absolute url provided by the serializer is not consistent
        if obj.head_image:
            return obj.head_image.url
        return None

    def get_back_image_url(self, obj):
        # This method will return the absolute URL for back_image if it's not null
        # used to get relative path beacause the absolute url provided by the serializer is not consistent
        if obj.back_image:
            return obj.back_image.url
        return None
