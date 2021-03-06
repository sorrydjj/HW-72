from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(label="email", widget=forms.EmailInput, required=True)


    def clean(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")
        if not first_name:
            if not last_name:
                raise ValidationError("заполните хотя бы одно из полей: last_name, first_name")
        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")