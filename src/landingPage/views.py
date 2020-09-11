from django.shortcuts import render
from landingPage.models import ContactFormEntry


def homeView(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")
        email = request.POST.get("email", "")

        ContactFormEntry.objects.create(
            name=name, subject=subject, message=message, email=email
        )

    return render(request, "landingPage/index.html", {})

def dosa_page(request):
    return render(request, 'landingPage/dosamaam.html')

def director_page(request):
    return render(request, 'landingPage/directorsir.html')
