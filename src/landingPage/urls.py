from django.urls import path
from landingPage.views import homeView, dosa_page, director_page

urlpatterns = [
    path("", homeView, name="home-page"),
    path("dean-letter",dosa_page, name="dosa-page" ),
    path("director-letter", director_page, name="director-page"),
]
