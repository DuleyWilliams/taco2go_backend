""" A module for handling Rating requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import Topping

class ToppingView(ViewSet):
    """ Topping Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a sauce"""
        try:
            topping = Topping.objects.get(pk=pk)
            serializer = ToppingSerializer(topping)
            return Response(serializer.data)
        except Topping.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all sauces"""
        toppings = Topping.objects.all()
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a rating """
        # incoming_user = request.auth.user
        new_topping = Topping.objects.create(
            type=request.data["type"]
        )
        serializer = ToppingSerializer(new_topping)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a sauce """
        editing_topping = Topping.objects.get(pk=pk)
        
        editing_topping.type = request.data["type"]
        editing_topping.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a sauce """
        try:
            topping = Topping.objects.get(pk=pk)
            topping.delete()
        except Topping.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ToppingSerializer(serializers.ModelSerializer):
    """JSON serializer for sauce"""
    class Meta:
        model = Topping
        fields = (
            'id',
            'type',)