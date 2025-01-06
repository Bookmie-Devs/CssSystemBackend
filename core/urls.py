from django.urls import path
from core.views import ContactUsCreateView

urlpatterns = [
    path("contact-us/", ContactUsCreateView.as_view()),
]
