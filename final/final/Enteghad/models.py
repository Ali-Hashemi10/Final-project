from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    first_name =  models.CharField(max_length= 255)
    last_name = models.CharField(max_length=255)
    movie = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)






