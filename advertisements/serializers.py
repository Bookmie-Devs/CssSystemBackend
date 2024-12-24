from rest_framework.serializers import ModelSerializer
from advertisements.models import Advertisement


class AdsSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = ("is_active",)
