from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required, 254 characters maximum.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Verify if email exist in registration
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is associated with an existing account, try another one please.")
        return email


# For update email in profile
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Required, 254 characters maximum.")

    class Meta:
        model = User
        fields = ['email']

    # verify changed email, then check if there is another one similar to cancel
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "This email is associated with an existing account, try another one please.")
        return email
