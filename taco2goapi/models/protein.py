from django.db import models

class Protein(models.Model):
    type = models.CharField(max_length=55)