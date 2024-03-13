from django import forms
from .models import Feedback, User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        feilds = ["first_name", "last_name", "username", "email", "password" ]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["usermame", "password"]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [ "movie", "descrption"]
