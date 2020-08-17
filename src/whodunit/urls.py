from django.urls import path
from whodunit.views import *

urlpatterns = [
    path("", landing_page, name='landing'),
    path("stories/", stories_view, name='stories'),
    path("stories/<str:story_name>/", stories_base_view, name="story-landing"),
    path("stories/<str:story_name>/rulebook/", story_rulebook_view, name="story-rulebook"),
    path("stories/<str:story_name>/questions/<int:level>/", story_question_view, name="story-question")
]
