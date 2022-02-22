from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your forms here.

class register_form(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The email address you have provided already has an account associated with it.")
        return self.cleaned_data['email']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("The username you have provided already has an account associated with it.")
        return self.cleaned_data['username']

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(register_form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
