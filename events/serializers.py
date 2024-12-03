from rest_framework.serializers import Serializer, ModelSerializer
from events.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
