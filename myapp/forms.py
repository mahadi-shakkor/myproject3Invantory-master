from django import forms
from .models import User

class UserFormsignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']  # Include only essential fields
        widgets = {
            'password': forms.PasswordInput(),  # Mask the password field
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 6:  # Enforce a minimum password length
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password
    

from django import forms
from .models   import User

class LoginForm(forms.Form):
    userid = forms.IntegerField(label="User ID")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:  # You can enforce your own password validation rules
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password
