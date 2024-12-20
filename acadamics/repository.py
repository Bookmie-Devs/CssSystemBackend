from acadamics.models import Course, AcadamicSlides, PastQuestions, OnlineTutorialTips


class CourseRepository:
    model = Course.objects

    @classmethod
    def get_all(cls):
        return cls.model.all()


class SlidesRepository:
    model = AcadamicSlides.objects

    @classmethod
    def get_slides(cls, course_id):
        return cls.model.filter(course=course_id).all()


class PastQuestionsRepository:
    model = PastQuestions.objects

    @classmethod
    def get_questions(cls, course_id):
        return cls.model.filter(course=course_id).all()


class OnlineTutorialTipsRepository:
    model = OnlineTutorialTips.objects

    @classmethod
    def get_links(cls, course_id):
        return cls.model.filter(course=course_id)
