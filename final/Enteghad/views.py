from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, Feedback
from .forms import RegisterForm, LoginForm, FeedbackForm

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, "userpanel.html")
    else:
        return render(request, "index.html")
    

def user_panel(request):
    pass


def user_register(request):
    if request.user.is_authenticated:
        return redirect('userpanel')
        
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
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
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username = form.cleaned_data["username"],
                    password = form.cleaned_data["password"]
                )

                if user:
                    login(request, user)
                    return redirect("userpanel")
                else:
                    return render(request, "forms.html", {"form": form})
            else:
                return render(request, "forms.html", {"form": form})
        else:
            return render(request, "forms.html", {"form": LoginForm})


def user_logout(request):
    logout(request)
    return redirect("home")

def create_fb(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.object.get(id=request.user.id)
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = Feedback.objects.create(
                    first_name = user.first_name,
                    last_name = user.last_name,
                    movie = form.cleaned_data["movie"],
                    desription = form.cleaned_data["desciption"]
                )
                return redirect("userpanel") 
            else:
                return render(request, "forms.html", {"form": form})
        else:
            return render(request, "forms.html", {"form": FeedbackForm})
    else:
        #alan age login nabashe asan nabayad in optiono dashte bashe ke betune create kone
        pass

def user_fbs():
    '''inja alan bayad user betune object cfb ro baraye 
    khodesh zakhire kone va un bala tuye create bayad asssgn beshe be user fb ke sakhte mishe'''
    pass