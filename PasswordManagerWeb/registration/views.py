from django.shortcuts import render
from .forms import UserCreationFormWithEmail
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms


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
class ProfileUpdate(TemplateView):
    template_name = 'registration/profile_form.html'
