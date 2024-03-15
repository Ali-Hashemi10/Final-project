from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from.models import User, Feedback
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from .models import User

def index(request):
    if request.user.is_authenticated:
        return render(request, "userpanel.html")
    else:
        return render(request, "index.html")

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('login')
        else:
            return render(request, "forms.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "forms.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return render(request, "userpanel.html")  
        else:
            return render(request, "forms.html", {"form": form})
    else:
        form = AuthenticationForm()  
        return render(request, "forms.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('index')  

def create_fb(request):
    pass

def user_fbs(request):
    pass
