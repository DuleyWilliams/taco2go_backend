from django.db import models
from taco2goapi.models.restaurant import Restaurant
from taco2goapi.models.tacoLover import TacoLover

class MyNextUp(models.Model):
    tacoLoverId = models.ForeignKey(TacoLover, on_delete=models.CASCADE)
    restaurantId = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    myFaved = models.BooleanField()