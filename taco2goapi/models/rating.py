from django.db import models

class Rating(models.Model):
    type = models.CharField(max_length=55)