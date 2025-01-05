from academics.models import Course, AcademicSlides, PastQuestions, OnlineTutorialTips


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
