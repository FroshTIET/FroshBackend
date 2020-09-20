from django.shortcuts import redirect, render
from django.urls.base import reverse
from froshwall.models import Tweet
from django.contrib.auth.decorators import login_required
# Create your views here.


def videoWallView(request):
    queryset = Tweet.objects.filter(approved=True)

    return render(request, 'froshwall/wall.html', {"messages":queryset})


@login_required
def addMessageform(request):

    if request.method == "POST":
        content = request.POST.get('content')
        user = request.user

        Tweet.objects.create(content=content, user=user)

        return redirect(reverse('froshwall'))


    return render(request, 'froshwall/inputform.html')