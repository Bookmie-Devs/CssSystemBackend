from executives.views import ExecutiveListView
from django.urls import path

urlpatterns = [
    path("", ExecutiveListView.as_view(), name="executives"),
]
