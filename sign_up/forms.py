from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class register_form(UserCreationForm):
    email = forms.EmailField(required=True)

    field_order = ['username', 'email', 'password1', 'password2']

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(register_form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
