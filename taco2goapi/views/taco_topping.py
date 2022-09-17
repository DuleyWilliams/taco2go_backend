""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models.myBuiltTaco import MyBuiltTaco
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.topping import Topping
from taco2goapi.models.tacoTopping import TacoTopping
from django.contrib.auth.models import User

class TacoToppingView(ViewSet):
    """ My Built Tacos Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a built taco"""
        try:
            taco_topping = TacoTopping.objects.get(pk=pk)
            serializer = TacoToppingSerializer(taco_topping)
            return Response(serializer.data)
        except TacoTopping.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all built tacos"""
        taco_toppings = TacoTopping.objects.all()
        serializer = TacoToppingSerializer(taco_toppings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a built taco """
        topping = Topping.objects.get(id=request.data["toppingId_id"])
        my_built_taco = MyBuiltTaco.objects.get(id=request.data["myBuiltTacoId_id"])
        new_taco_topping = TacoTopping.objects.create(
            toppingId=topping,
            myBuiltTacoId=my_built_taco
        )
        serializer = TacoToppingSerializer(new_taco_topping)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_taco_topping = TacoTopping.objects.get(pk=pk)
        editing_taco_topping.myBuiltTacoId_id = request.data["myBuiltTacoId_id"]
        editing_taco_topping.toppingId_id = request.data["toppingId_id"]
        editing_taco_topping.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a menu item """
        try:
            taco_topping = TacoTopping.objects.get(pk=pk)
            taco_topping.delete()
        except TacoTopping.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class TacoToppingSerializer(serializers.ModelSerializer):
    """JSON serializer for tacotopping types"""
    class Meta:
        model = TacoTopping
        fields = (
            'id',
            'myBuiltTacoId_id',
            'toppingId_id'
            )