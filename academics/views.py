from django.shortcuts import render
from academics.serializers import (
    CourseSerializer,
    CourseResourceSerializer,
    OnlineTutorialTipsSerializer,
    PastQuestionsSerializer,
    SlidesSerializer,
    InternshipOpportunitiesSerializer,
)
from academics.repository import CourseRepository
from rest_framework.generics import ListAPIView
from academics.repository import (
    OnlineTutorialTipsRepository,
    SlidesRepository,
    PastQuestionsRepository,
    InternshipOpportunitiesRepository,
)
from rest_framework.response import Response

# Create your views here.


class GetAllCoursesView(ListAPIView):
    repo = CourseRepository
    serializer_class = CourseSerializer
    queryset = repo.get_all()


class GetCourseResourcesView(ListAPIView):
    online_tips_repo = OnlineTutorialTipsRepository
    past_que_repo = PastQuestionsRepository
    slides_repo = SlidesRepository

    # serializers
    # sc = serializer
    slides_sc = SlidesSerializer
    online_tips_sc = OnlineTutorialTipsSerializer
    past_que_sc = PastQuestionsSerializer

    def get(self, request, course_id):
        online_tutorial_tips = self.online_tips_repo.get_links(course_id=course_id)
        past_questions = self.past_que_repo.get_questions(course_id=course_id)
        slides = self.slides_repo.get_slides(course_id=course_id)

        data = {
            "online_tutorial_tips": self.online_tips_sc(
                online_tutorial_tips, many=True
            ).data,
            "past_questions": self.past_que_sc(past_questions, many=True).data,
            "slides": self.slides_sc(slides, many=True).data,
        }
        return Response(data=data)


class InternshipOpportunitiesListView(ListAPIView):
    serializer_class = InternshipOpportunitiesSerializer
    queryset = InternshipOpportunitiesRepository.get_all_internship_opportunities()
