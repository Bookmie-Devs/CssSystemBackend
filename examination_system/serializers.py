from rest_framework.serializers import Serializer, ModelSerializer
from examination_system.models import ExaminationSchedule


class ExaminationScheduleSerializer(ModelSerializer):
    class Meta:
        model = ExaminationSchedule
        fields = "__all__"
