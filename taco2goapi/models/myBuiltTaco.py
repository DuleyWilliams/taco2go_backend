from django.db import models
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.shell import Shell
from taco2goapi.models.protein import Protein

class MyBuiltTaco(models.Model):
    tacoLoverId = models.ForeignKey(TacoLover, on_delete=models.CASCADE)
    tacoShellId = models.ForeignKey(Shell, on_delete=models.CASCADE)
    tacoProteinId = models.ForeignKey(Protein, on_delete=models.CASCADE)
    