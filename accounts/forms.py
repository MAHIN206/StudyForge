from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email'
        })
    )

    full_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name'
        })
    )

    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date'
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'full_name',
            'date_of_birth',
            'password1',
            'password2'
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            Profile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                date_of_birth=self.cleaned_data['date_of_birth']
            )

        return user