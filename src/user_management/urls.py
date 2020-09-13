from django.contrib.messages import api
from django.urls import path
from rest_framework.authtoken.views import *

from user_management.views import (
    LeaderBoard,
    MyDetailsView,
    StudentDetailView,
    StudentListView,
    api_root,
    setFireBaseToken,
)

from django.contrib.auth.views import (
    LogoutView, PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    LoginView,
)

urlpatterns = [
    path("api/", api_root, name="api-root"),
    path("api/api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/students/", StudentListView.as_view(), name="student-list"),
    path("api/student/<uuid:pk>/", StudentDetailView.as_view(), name="student-details"),
    path("api/student/detail/", MyDetailsView.as_view(), name="my-details"),
    path("api/leaderboard/", LeaderBoard.as_view(), name="leaderboard"),
    path("api/pushToken/", setFireBaseToken.as_view(), name="set-token"),
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        PasswordChangeView.as_view(template_name="registration/password_change.html"),
        name="password_change",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("login/", LoginView.as_view(), name='login' ),
    path("logout/", LogoutView.as_view(next_page="/"), name='logout')
]
