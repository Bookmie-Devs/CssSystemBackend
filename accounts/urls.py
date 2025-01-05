from django.urls import path
from accounts.views import (
    RegisterView,
    SaveBlogView,
    UserProfileView,
    LoginView,
    GetUserSavedBlogs,
    RemoveSavedBlogView,
)
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
    path("save-blog/", SaveBlogView.as_view(), name="save-blog"),
    path("saved-blogs/", GetUserSavedBlogs.as_view(), name="user-saved-blogs"),
    path(
        "removed-saved-blog/<news_blog_id>/",
        RemoveSavedBlogView.as_view(),
        name="removed-blog",
    ),
    # path("saved-resources/"),
]
