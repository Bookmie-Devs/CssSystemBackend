from events.models import Event


class EventRepo:
    model = Event.objects

    @classmethod
    def get_all_events(cls):
        return cls.model.filter()
