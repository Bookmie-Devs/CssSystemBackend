from events.views import EventListView
from django.urls import path

urlpatterns = [
    path("", EventListView.as_view(), name="events"),
]
