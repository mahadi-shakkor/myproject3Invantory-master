from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class CustomUserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    # Checkbox fields for user types
    f = forms.BooleanField(required=False, label="Field F")
    s = forms.BooleanField(required=False, label="Field S")
    n = forms.BooleanField(required=False, label="Field N")
    w = forms.BooleanField(required=False, label="Field W")
    c = forms.BooleanField(required=False, label="Field C")
    d = forms.BooleanField(required=False, label="Field D")
    r = forms.BooleanField(required=False, label="Field R")
    a = forms.BooleanField(required=False, label="Field A")

    location = forms.ModelChoiceField(queryset=User.objects.none(), required=False, label="Location")  # Adjust for location

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password', 'f', 's', 'n', 'w', 'c', 'd', 'r', 'a', 'location']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Hash the password
        user.password = make_password(self.cleaned_data['password'])

        # Map checkbox values to "f", "s", etc., or "" if not selected
        user.f = "F" if self.cleaned_data['f'] else ""
        user.s = "S" if self.cleaned_data['s'] else ""
        user.n = "N" if self.cleaned_data['n'] else ""
        user.w = "W" if self.cleaned_data['w'] else ""
        user.c = "C" if self.cleaned_data['c'] else ""
        user.d = "D" if self.cleaned_data['d'] else ""
        user.r = "R" if self.cleaned_data['r'] else ""
        user.a = "A" if self.cleaned_data['a'] else ""

        if commit:
            user.save()
        return user
