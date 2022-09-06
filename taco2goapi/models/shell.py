from django.db import models

class Shell(models.Model):
    type = models.CharField(max_length=55)