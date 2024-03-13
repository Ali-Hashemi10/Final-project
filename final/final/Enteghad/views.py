from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from.models import User, Feedback

# Create your views here.

def user_register(request):
    if request.user.is_authenticated:
        # return redirect('home/profile/')
        pass
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    first_name = form.cleaned_data['first-name'],
                    last_name = form.cleaned_data['last_name'],
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['passwords']
                )
                login(request, user)
                # return redirect(request, "user_panel.html")
            else:
                return render(request, "forms.html", {"form":form})
        else:
            return render(request, "forms.html", {"form":RegisterForm})   

def user_login():
    pass

def user_logout():
    pass

def create_fb():
    pass

def user_fbs():
    pass
