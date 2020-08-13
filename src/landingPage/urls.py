from django.urls import path
from landingPage.views import homeView

urlpatterns = [
    path("", homeView, name="home-page"),
]
