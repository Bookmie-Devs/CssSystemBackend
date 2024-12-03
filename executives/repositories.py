from executives.models import Executive


class ExecutiveRepo:
    model = Executive.objects

    @classmethod
    def get_all(cls):
        return cls.model.filter().all()
