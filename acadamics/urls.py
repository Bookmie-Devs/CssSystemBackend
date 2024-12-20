from django.urls import path
from acadamics.views import GetAllCoursesView, GetCourseResourcesView

urlpatterns = [
    path("courses/", GetAllCoursesView.as_view(), name="all_courses"),
    path(
        "courses/<course_id>/", GetCourseResourcesView.as_view(), name="get-resources"
    ),
]
