from django.db import models
from taco2goapi.models.sauce import Sauce
from taco2goapi.models.myBuiltTaco import MyBuiltTaco

class TacoSauce(models.Model):
    myBuiltTacoId = models.ForeignKey(MyBuiltTaco, on_delete=models.CASCADE, related_name="taco_sauces")
    sauceId = models.ForeignKey(Sauce, on_delete=models.CASCADE, related_name="taco_sauces")