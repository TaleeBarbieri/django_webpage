from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='*Required. Max 30 Characters')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='*Required. Inform a valid email address.')
    phone_number = forms.CharField(help_text='*Required. Inform a valid phone number.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2', )
