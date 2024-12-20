from rest_framework.serializers import ModelSerializer, Serializer
from acadamics.models import Course, AcadamicSlides, OnlineTutorialTips, PastQuestions


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SlidesSerializer(ModelSerializer):
    class Meta:
        model = AcadamicSlides
        fields = "__all__"


class OnlineTutorialTipsSerializer(ModelSerializer):
    class Meta:
        model = OnlineTutorialTips
        fields = "__all__"


class PastQuestionsSerializer(ModelSerializer):
    class Meta:
        model = PastQuestions
        fields = "__all__"


class CourseResourceSerializer(Serializer):
    # slides = SlidesSerializer()
    online_tutorila_tips = OnlineTutorialTips()
    past_questions = PastQuestionsSerializer()
