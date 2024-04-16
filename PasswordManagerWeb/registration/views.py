from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import UserCreationFormWithEmail, EmailForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        # Modify form
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Write your username here...'})
        form.fields['email'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Write your email here...'})
        form.fields['password1'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'type': 'password', 'placeholder': 'Write your password here...'})
        form.fields['password2'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'type': 'password', 'placeholder': 'Repeat your password here...'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = [
        'avatar', 'link'
    ]
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Get user ID
    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        context['user_data'] = user
        return context


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    # Get user
    def get_object(self, queryset=None):
        return self.request.user

    #modify template email
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'}
        )
        return form
