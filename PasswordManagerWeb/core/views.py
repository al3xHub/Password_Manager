from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Site
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse


# Create your views here.
@login_required
def home(request):
    user = request.user
    sites = Site.objects.filter(user=user)
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


def site(request, pk):
    try:
        sites = Site.objects.get(id=pk)
        context = {
            'sites': sites
        }
    except:
        return redirect("home")
    return render(request, "core/site.html", context)


class SiteUpdate(UpdateView):
    model = Site
    fields = [
        'website_name', 'website_link', 'website_username', 'website_password',
        'website_notes'
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('site', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super(SiteUpdate, self).get_form()

        # Modify form
        form.fields['website_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_link'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_password'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_notes'].widget = forms.Textarea(
            attrs={'class': 'form-control mb-2'})
        return form


# Create sites logic
class CreateSite(LoginRequiredMixin, CreateView):
    model = Site
    fields = [
        'website_name', 'website_link', 'website_username', 'website_password',
        'website_notes'
    ]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Delete Site
class DeleteSite(DeleteView):
    model = Site
    success_url = reverse_lazy('home')
