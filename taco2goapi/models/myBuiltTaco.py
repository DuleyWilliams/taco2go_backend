from django.db import models
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.shell import Shell
from taco2goapi.models.protein import Protein

class MyBuiltTaco(models.Model):
    name = models.CharField(max_length=55, default="")
    tacoLoverId = models.ForeignKey(TacoLover, on_delete=models.CASCADE)
    tacoShellId = models.ForeignKey(Shell, on_delete=models.CASCADE)
    tacoProteinId = models.ForeignKey(Protein, on_delete=models.CASCADE)
    
    @property
    def sauces(self):
        taco_sauces=self.taco_sauces.all()
        
        return [ts.sauceId for ts in taco_sauces]
    
    @property
    def toppings(self):
        taco_toppings=self.taco_toppings.all()
        return [tt.toppingId for tt in taco_toppings]
    