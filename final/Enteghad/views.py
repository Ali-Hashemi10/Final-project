from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import User, Feedback
from .forms import RegisterForm, FeedbackForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("userpanel")
    else:
        return render(request, "index.html")
    

def user_panel(request):
    user = request.user.username
    return render(request, "userpanel.html", {"username":user})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('userpanel')
        
    else:
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
                return redirect("userpanel")
            else:
                return render(request, "forms.html", {"form":form})
        else:
            return render(request, "forms.html", {"form":RegisterForm})   

def user_login(request):
    if request.user.is_authenticated: 
       return redirect("userpanel")
    else:
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
    return redirect("home")

def create_fb(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(id=request.user.id)
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = Feedback.objects.create(
                    first_name = user.first_name,
                    last_name = user.last_name,
                    movie = form.cleaned_data["movie"],
                    description = form.cleaned_data["description"],
                    creator = user
                )
                return redirect("userpanel") 
            else:
                return render(request, "forms.html", {"form": form})
        else:
            return render(request, "forms.html", {"form": FeedbackForm})
    else:
        return redirect("login")
      

def user_fbs(request):
    feedbacks = Feedback.objects.filter(creator_id=request.user.id)
    return render(request, "userfbs.html", {'objects':feedbacks})
    