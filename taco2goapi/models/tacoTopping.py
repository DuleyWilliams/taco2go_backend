from django.db import models
from taco2goapi.models.topping import Topping
from taco2goapi.models.myBuiltTaco import MyBuiltTaco

class TacoTopping(models.Model):
    myBuiltTacoId = models.ForeignKey(MyBuiltTaco, on_delete=models.CASCADE, related_name="taco_toppings")
    toppingId = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="taco_toppings")