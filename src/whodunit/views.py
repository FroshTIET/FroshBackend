from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from whodunit.models import Question

# Create your views here.

story_name_dict = {"space": 1, "murder": 2, "vexed": 3}


def landing_page(request):
    return render(request, 'whodunit/landing.html', {})


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
    if story_name == "space":
        return render(request, 'whodunit/story_rulebook_space.html', {})
    elif story_name == "murder":
        return render(request, 'whodunit/story_rulebook_murder.html', {})
    elif story_name == "vexed":
        return render(request, 'whodunit/story_rulebook_vexed.html', {})



@login_required
def story_question_view(request, story_name, level):
    user_level = request.user.score.get_wh_level(story_name_dict[story_name])
    print(user_level)

    if user_level != level - 1:
        return redirect(reverse("story-question", args=(story_name, user_level + 1)))

    currentQuestion = Question.objects.get(story=story_name, level=level)

    if request.method == "POST":
        submitted_answer = request.POST.get('answer', '')
        if submitted_answer == currentQuestion.answer_field:
            request.user.score.inc_wh_level(story_name_dict[story_name])
            return redirect(reverse("story-question", args=(story_name, level+1)))
        else: 
            messages.error(request, 'The answer was incorrect. Please try again')
    return render(request, 'whodunit/questionTemplate.html', {"question":currentQuestion})