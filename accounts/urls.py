from django.urls import path
from accounts.views import (
    RegisterView,
    SaveBlogView,
    UserProfileView,
    LoginView,
    GetUserSavedBlogs,
    RemoveSavedBlogView,
    GetUserSavedAcademicResources,
    RemoveSavedOnlineResourceTipsView,
    RemoveSavedSlidesView,
    SaveOnlineTipResourceView,
    SaveSlideResourceView,
    SavePastQuestionResourceView,
    RemoveSavedPastQuestionsView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from accounts.executive_door import excutive_door

app_name = "accounts"

urlpatterns = [
    # executive dor way
    path("executive-door/", excutive_door, name="executive-door"),
    # User Authentication URLs
    path("register/", RegisterView.as_view(), name="register"),
    path("obtain-token/", LoginView.as_view(), name="obtain-token"),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
    path("verify-token/", TokenVerifyView.as_view(), name="token-verify"),
    # User Profile URLs
    path("profile/", UserProfileView.as_view(), name="profile"),
    # Saved Blogs URLs
    path("save-blog/", SaveBlogView.as_view(), name="save-blog"),
    path("saved-blogs/", GetUserSavedBlogs.as_view(), name="user-saved-blogs"),
    path(
        "removed-saved-blog/<news_blog_id>/",
        RemoveSavedBlogView.as_view(),
        name="removed-blog",
    ),
    # Saved Resources URLs
    path(
        "save-online-tutotial-tips/",
        SaveOnlineTipResourceView.as_view(),
        name="save-online-tip",
    ),
    path(
        "remove-online-tutorial-tip/<online_tip_id>/",
        RemoveSavedOnlineResourceTipsView.as_view(),
        name="remove-online-tip",
    ),
    path("save-slide/", SaveSlideResourceView.as_view(), name="save-slide"),
    path(
        "remove-saved-slide/<int:slide_id>/",
        RemoveSavedSlidesView.as_view(),
        name="remove-saved-slide",
    ),
    path(
        "save-past-question/",
        SavePastQuestionResourceView.as_view(),
        name="save-past-question",
    ),
    path(
        "remove-saved-past-question/<int:past_question_id>/",
        RemoveSavedPastQuestionsView.as_view(),
        name="remove-saved-past-question",
    ),
    # Saved Academic Resources URL
    path(
        "saved-resources/",
        GetUserSavedAcademicResources.as_view(),
        name="saved-academic-resources",
    ),
]
