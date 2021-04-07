from django import forms

# Models
from django.contrib.auth.models import User

from users.models import Profile


class SingupForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput
    )
    password_confirmation = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput  # El Widget para hacer comprobaciones
    )
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    def clean_username(self):
        """Username must be:
        - Unique
        """

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already taken')
        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

    def save(self):
        """Create User and Profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
