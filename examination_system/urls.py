from django.urls import path
from examination_system.views import GetExamSchedules

urlpatterns = [
    path("shedules/", GetExamSchedules.as_view(), name="shedules"),
]
