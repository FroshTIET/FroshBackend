from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

story_name_dict = {"space": 1, "murder": 2, "vexed": 3}


def landing_page(request):
    return HttpResponse("Hello World")


@login_required
def stories_view(request):
    return HttpResponse(
        """
    
    <a href="/whodunit/stories/space">Story 1</a>
    <a href="/whodunit/stories/murder">Story 2</a>
    <a href="/whodunit/stories/vexed">Story 3</a>
    
    
    """
    )


@login_required
def stories_base_view(request, story_name):
    print(story_name)
    return HttpResponse(f"You are on the {story_name} story")


@login_required
def story_rulebook_view(request, story_name):
    return HttpResponse(f"You are viewing {story_name}'s rulebook")


@login_required
def story_question_view(request, story_name, level):
    user_level = request.user.score.get_wh_level(story_name_dict[story_name])
    request.user.score.inc_wh_level(story_name_dict[story_name])
    print(user_level)

    # if request.user.score.whodunit_level != level - 1:
    #     return redirect(reverse("story-question", args=(story_name,)))

    return HttpResponse(f"You are viewing question {level} of {story_name}")
