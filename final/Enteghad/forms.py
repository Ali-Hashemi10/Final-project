from django import forms
from .models import Feedback, User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password" ]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["movie", "description"]