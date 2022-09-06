from django.db import models

class Topping(models.Model):
    type = models.CharField(max_length=55)