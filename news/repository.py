from news.models import News


class NewsRepository:
    model = News.objects

    @classmethod
    def get_all(cls):
        return cls.model.all()
