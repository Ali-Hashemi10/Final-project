from django.urls import path
from .views import user_register, user_login, user_logout, create_fb, user_fbs

urlpatterns = [
    path("home/signup/", user_register, name="register"),
    path("home/login/", user_login, name="login"),
    #bayad yechi dashte bashim baraye user panel
    path("home/profile/new-feedback/", create_fb, name="create-fb"),
    path("home/profile/my-feedbacks/", user_fbs, name="feedbacks"),

]