from rest_framework.serializers import Serializer, ModelSerializer
from examination_system.models import ExaminationSchedule
from acadamics.serializers import CourseSerializer


class ExaminationScheduleSerializer(ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = ExaminationSchedule
        fields = "__all__"
