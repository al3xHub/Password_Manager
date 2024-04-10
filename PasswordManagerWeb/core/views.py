from django.shortcuts import render
from .models import Site


# Create your views here.
def home(request):
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, "core/home.html", context)


def profile(request):
    return render(request, "core/profile.html")


def add(request):
    return render(request, "core/add.html")


def login(request):
    return render(request, "core/login.html")


def logout(request):
    return render(request, "core/logout.html")


def register(request):
    return render(request, "core/register.html")


def site(request):
    return render(request, "core/site.html")
