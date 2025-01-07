from academics.models import (
    Course,
    AcademicSlides,
    PastQuestions,
    OnlineTutorialTips,
    InternshipOpportunities,
)


class CourseRepository:
    model = Course.objects

    @classmethod
    def get_all(cls):
        return cls.model.all()


class SlidesRepository:
    model = AcademicSlides.objects

    @classmethod
    def get_slides(cls, course_id):
        return cls.model.filter(course=course_id).all()

    @classmethod
    def get_slide(cls, pk):
        try:
            return cls.model.get(pk=pk)
        except:
            return None


class PastQuestionsRepository:
    model = PastQuestions.objects

    @classmethod
    def get_questions(cls, course_id):
        return cls.model.filter(course=course_id).all()

    @classmethod
    def get_past_question(cls, pk):
        try:
            return cls.model.get(pk=pk)
        except:
            return None


class InternshipOpportunitiesRepository:
    model = InternshipOpportunities.objects

    @classmethod
    def get_all_internship_opportunities(cls):
        return cls.model.all()

    @staticmethod
    def get_internship_by_id(cls, internship_id):
        return cls.model.get(id=internship_id)


class OnlineTutorialTipsRepository:
    model = OnlineTutorialTips.objects

    @classmethod
    def get_links(cls, course_id):
        return cls.model.filter(course=course_id)

    @classmethod
    def get_online_tip(cls, pk):
        try:
            return cls.model.get(pk=pk)
        except:
            return None
