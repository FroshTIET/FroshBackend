from django.urls import path

from froshwall.views import addMessageform, videoWallView

urlpatterns = [
    path("", videoWallView, name='froshwall'),
    path("submit", addMessageform, name='form'),
]
