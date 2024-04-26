from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe

from .models import Site
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse


# Create your views here.
@method_decorator(login_required, name='dispatch')
class HomeListView(ListView):
    model = Site
    paginate_by = 7
    template_name = 'core/home.html'
    context_object_name = 'sites'

    def get_queryset(self):
        user = self.request.user
        queryset = Site.objects.filter(user=user)
        return queryset

    def post(self, request, *args, **kwargs):
        user = request.user
        search_term = request.POST.get('search')
        queryset = Site.objects.filter(user=user)

        if search_term:
            queryset = queryset.filter(
                Q(website_name__icontains=search_term) |
                Q(website_username__icontains=search_term) |
                Q(website_link__icontains=search_term)
            )
            if not queryset.exists():
                return redirect("home")

        context = {'sites': queryset}
        return render(request, self.template_name, context)


def profile(request):
    return render(request, "core/profile.html")


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


class SiteUpdateForm(forms.ModelForm):
    password_repeat = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}))

    class Meta:
        model = Site
        fields = ['website_name', 'website_link', 'website_username', 'website_notes', 'website_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'website_password' in self.fields:
            website_password_value = self.instance.website_password
            self.fields['password_repeat'].widget.attrs['value'] = website_password_value

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("website_password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            self.add_error('password_repeat', "Passwords do not match")


class SiteUpdate(UpdateView):
    model = Site
    form_class = SiteUpdateForm
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
            attrs={'type': 'password', 'class': 'form-control mb-2'})
        form.fields['website_notes'].widget = forms.Textarea(
            attrs={'class': 'form-control mb-2'})
        return form

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Site updated successfully.')
            return response
        except Exception as e:
            messages.error(self.request, f'Error updating site: {str(e)}')
            return self.response_class(
                request=self.request,
                template_name=self.template_name,
                context=self.get_context_data(form=form),
                status=400
            )


# Create sites logic
class CreateSite(LoginRequiredMixin, CreateView):
    model = Site
    template_name = "core/site_form.html"
    fields = [
        'website_name', 'website_link', 'website_username', 'website_password',
        'website_notes'
    ]

    required = {
        'website_link': False,
        'website_notes': False,
    }

    def get_form(self, form_class=None):
        form = super(CreateSite, self).get_form()

        # Modify form
        form.fields['website_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_link'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2'})
        form.fields['website_password'].widget = forms.TextInput(
            attrs={'type': 'password', 'class': 'form-control mb-2'})
        form.fields['website_notes'].widget = forms.Textarea(
            attrs={'class': 'form-control mb-2'})
        return form

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            messages.success(self.request, 'Site created successfully!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Error: {str(e)}')
            return self.form_invalid(form)


# Delete Site
class DeleteSite(DeleteView):
    model = Site
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(self.request, 'Site deleted successfully.')
            return response
        except Exception as e:
            messages.error(self.request, f'Error deleting site: {str(e)}')
            return self.response_class(
                request=self.request,
                template_name=self.template_name,
                context=self.get_context_data(),
                status=400
            )
