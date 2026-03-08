from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data.get('email')

        if commit:
            user.save()

            # Save full name in Profile
            profile = user.profile
            profile.full_name = self.cleaned_data.get('full_name')
            profile.save()

        return user