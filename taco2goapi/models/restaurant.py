from django.db import models

class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=55)
    address = models.CharField(max_length=55)
    zipCode = models.CharField(max_length=10)
    phone = models.CharField(max_length=7)
    website = models.URLField()
    email = models.EmailField()
    stateName = models.CharField(max_length=2)
    cityName = models.CharField(max_length=55)
    cuisineType = models.CharField(max_length=55)
    hoursInterval = models.CharField(max_length=55)