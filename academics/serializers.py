from rest_framework.serializers import ModelSerializer, Serializer
from academics.models import (
    Course,
    AcademicSlides,
    OnlineTutorialTips,
    PastQuestions,
    InternshipOpportunities,
)


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SlidesSerializer(ModelSerializer):
    class Meta:
        model = AcademicSlides
        fields = "__all__"


class InternshipOpportunitiesSerializer(ModelSerializer):
    class Meta:
        model = InternshipOpportunities
        fields = [
            "internship_id",
            "campany_name",
            "description",
            "registration_link",
            "application_deadline",
            "created_at",
        ]
        read_only_fields = ["created_at"]


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
