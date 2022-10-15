""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models.myBuiltTaco import MyBuiltTaco
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.shell import Shell
from taco2goapi.models.protein import Protein
from django.contrib.auth.models import User
from taco2goapi.models.tacoSauce import TacoSauce
from taco2goapi.models.sauce import Sauce

from taco2goapi.models.tacoTopping import TacoTopping
from taco2goapi.models.topping import Topping

class MyBuiltTacoView(ViewSet):
    """ My Built Tacos Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a built taco"""
        try:
            my_built_taco = MyBuiltTaco.objects.get(pk=pk)
            serializer = MyBuiltTacoSerializer(my_built_taco)
            return Response(serializer.data)
        except MyBuiltTaco.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all built tacos"""
        my_built_tacos = MyBuiltTaco.objects.all()
        serializer = MyBuiltTacoSerializer(my_built_tacos, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a built taco """
        user = TacoLover.objects.get(user=request.auth.user)
        protein = Protein.objects.get(id=request.data["protein_id"])
        shell = Shell.objects.get(id=request.data["shell_id"])
        new_my_built_taco = MyBuiltTaco.objects.create(
            name=request.data["name"],
            tacoLoverId=user,
            tacoProteinId=protein,
            tacoShellId=shell
        )
        topping_ids = request.data["topping_ids"]
        for topping_id in topping_ids:
            TacoTopping.objects.create(
                toppingId=Topping.objects.get(pk=topping_id),
                myBuiltTacoId=new_my_built_taco
            )
        sauce_ids = request.data["sauce_ids"]
        for sauce_id in sauce_ids:
            TacoSauce.objects.create(
                sauceId=Sauce.objects.get(pk=sauce_id),
                myBuiltTacoId=new_my_built_taco
            )
        serializer = MyBuiltTacoSerializer(new_my_built_taco)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_my_built_taco = MyBuiltTaco.objects.get(pk=pk)
        
        editing_my_built_taco.tacoLoverId_id = request.data["tacoLoverId_id"]
        editing_my_built_taco.tacoProteinId_id = request.data["tacoProteinId_id"]
        editing_my_built_taco.tacoShellId_id = request.data["tacoShellId_id"]
        editing_my_built_taco.name = request.data["name"]
        editing_my_built_taco.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a menu item """
        try:
            my_built_taco = MyBuiltTaco.objects.get(pk=pk)
            my_built_taco.delete()
        except MyBuiltTaco.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauce
        fields = (
            'id',
            'type')

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            'id',
            'type')
    
class MyBuiltTacoSerializer(serializers.ModelSerializer):
    """JSON serializer for mybuilttacos types"""
    sauces = SauceSerializer(many=True)
    toppings = ToppingSerializer(many=True)
    class Meta:
        depth = 1
        model = MyBuiltTaco
        fields = (
            'id',
            'tacoLoverId',
            'tacoProteinId',
            'tacoShellId',
            'name',
            'sauces',
            'toppings')