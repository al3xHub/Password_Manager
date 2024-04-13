from django.shortcuts import render, redirect
from .models import Site
from django.views.generic import CreateView


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
    return render(request, "core/site_form.html")


def login(request):
    return render(request, "core/login.html")


def logout(request):
    return render(request, "core/logout.html")


def register(request):
    return render(request, "core/register.html")


def site(request, pk):
    try:
        sites = Site.objects.get(id=pk)
        context = {
            'sites': sites
        }
    except:
        return redirect("home")
    return render(request, "core/site.html", context)


#Create sites logic
class CreateSite(CreateView):
    model = Site
    fields = [
        'website_name', 'website_link', 'website_username', 'website_password',
        'website_notes'
    ]
