from django.urls import path
from .views import user_register, user_login, user_logout, create_fb, user_fbs, index, user_panel

urlpatterns = [
    path("home/", index, name="home"),
    path("home/signup/", user_register, name="register"),
    path("home/login/", user_login, name="login"),
    path("home/profile/", user_panel, name="userpanel"),
    path("home/profile/new-feedback/", create_fb, name="create-fb"),
    path("home/profile/my-feedbacks/", user_fbs, name="feedbacks"),
    path("home/logout/", user_logout, name="logout"),

]

# /<int:id>
# def index(request, id)
#     slug