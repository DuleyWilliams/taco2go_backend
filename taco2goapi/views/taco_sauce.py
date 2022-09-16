""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models.myBuiltTaco import MyBuiltTaco
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.sauce import Sauce
from taco2goapi.models.tacoSauce import TacoSauce
from django.contrib.auth.models import User

class TacoSauceView(ViewSet):
    """ My Built Tacos Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a built taco"""
        try:
            taco_sauce = TacoSauce.objects.get(pk=pk)
            serializer = TacoSauceSerializer(taco_sauce)
            return Response(serializer.data)
        except TacoSauce.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all built tacos"""
        taco_sauces = TacoSauce.objects.all()
        serializer = TacoSauceSerializer(taco_sauces, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a built taco """
        sauce = Sauce.objects.get(id=request.data["sauceId_id"])
        my_built_taco = MyBuiltTaco.objects.get(id=request.data["myBuiltTacoId_id"])
        new_taco_sauce = TacoSauce.objects.create(
            sauceId=sauce,
            myBuiltTacoId=my_built_taco
        )
        serializer = TacoSauceSerializer(new_taco_sauce)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_taco_sauce = TacoSauce.objects.get(pk=pk)
        editing_taco_sauce.myBuiltTacoId_id = request.data["myBuiltTacoId_id"]
        editing_taco_sauce.sauceId_id = request.data["sauceId_id"]
        editing_taco_sauce.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a menu item """
        try:
            taco_sauce = TacoSauce.objects.get(pk=pk)
            taco_sauce.delete()
        except TacoSauce.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class TacoSauceSerializer(serializers.ModelSerializer):
    """JSON serializer for mybuilttacos types"""
    class Meta:
        model = TacoSauce
        fields = (
            'id',
            'myBuiltTacoId_id',
            'sauceId_id'
            )