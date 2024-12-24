from rest_framework.serializers import Serializer, ModelSerializer
from events.models import Event
from timeline.serializers import TimelineSerializer

class EventSerializer(ModelSerializer):
    timeline = TimelineSerializer(many=True)
    class Meta:
        model = Event
        fields = "__all__"
