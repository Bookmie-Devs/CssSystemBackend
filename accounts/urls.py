from django.urls import path
from accounts.views import RegisterView, UserProfileView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("obtain-token/", LoginView.as_view(), name="obtain-token"),
    path("refresh-token", TokenRefreshView.as_view(), name="refresh-token"),
    path("verify-token/", TokenVerifyView.as_view(), name="token-verify"),
]
