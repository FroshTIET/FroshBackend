from django.urls import path, include
from rest_framework.authtoken.views import *

from user_management.views import (
    LeaderBoard,
    MyDetailsView,
    StudentDetailView,
    StudentListView,
    api_root,
)

urlpatterns = [
    path("", api_root, name="api-root"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("student/<uuid:pk>/", StudentDetailView.as_view(), name="student-details"),
    path("student/detail/", MyDetailsView.as_view(), name="my-details"),
    path("leaderboard/", LeaderBoard.as_view(), name="leaderboard"),
]
