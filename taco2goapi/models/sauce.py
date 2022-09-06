from django.db import models

class Sauce(models.Model):
    type = models.CharField(max_length=55)