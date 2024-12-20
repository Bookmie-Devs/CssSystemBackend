from news.models import News
from rest_framework.serializers import ModelSerializer, Serializer


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
