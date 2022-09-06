from django.db import models
from django.contrib.auth.models import User

class TacoLover(models.Model):
    taco_lover = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.URLField(max_length=200)
    userCity = models.CharField(max_length=50)
    email = models.EmailField()
    userState = models.CharField(max_length=2)