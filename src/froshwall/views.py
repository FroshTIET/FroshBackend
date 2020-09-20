from django.shortcuts import redirect, render
from django.urls.base import reverse
from froshwall.models import Tweet
from django.contrib.auth.decorators import login_required
from .forms import FormWithCaptcha
from django.contrib import messages
from django.conf import settings
import requests

# Create your views here.


def videoWallView(request):
    queryset = Tweet.objects.filter(approved=True)

    return render(request, "froshwall/wall.html", {"tweets": queryset})


def addMessageform(request):

    if request.method == "POST":
        form = FormWithCaptcha(request.POST)
        content = request.POST.get("content")
        user = request.POST.get("username")
        """ Begin reCAPTCHA validation """
        recaptcha_response = request.POST.get("g-recaptcha-response")
        url = "https://www.google.com/recaptcha/api/siteverify"
        values = {
            "secret": settings.RECAPTCHA_PRIVATE_KEY,
            "response": recaptcha_response,
        }

        response = requests.post(url, data=values)

        """ End reCAPTCHA validation """
        if response.json()["success"] == False:
            messages.warning(request, "ReCaptcha Verification failed. Please try again.")
            return redirect(reverse("froshwall"))
        else:

            Tweet.objects.create(content=content, username=user)
            messages.success(request, "Your message has been received, and will be updated shortly.")
            return redirect(reverse("froshwall"))
    else:
        form = FormWithCaptcha()

    return render(request, "froshwall/inputform.html", {"form": form})

