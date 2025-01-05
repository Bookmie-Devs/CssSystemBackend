from executives.models import Executive


class ExecutiveRepo:
    model = Executive.objects

    @classmethod
    def get_all_active(cls):
        return cls.model.filter(is_active=True).all()
