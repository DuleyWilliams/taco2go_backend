from django.db import models
from taco2goapi.models.rating import Rating
from taco2goapi.models.restaurant import Restaurant
from taco2goapi.models.tacoLover import TacoLover

class MyFavs(models.Model):
    tacoLoverId = models.ForeignKey(TacoLover, on_delete=models.CASCADE)
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ratingId = models.ForeignKey(Rating, on_delete=models.CASCADE)