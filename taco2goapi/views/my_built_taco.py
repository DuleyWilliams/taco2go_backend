""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models.myBuiltTaco import MyBuiltTaco
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.shell import Shell
from taco2goapi.models.protein import Protein
from django.contrib.auth.models import User

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
        protein = Protein.objects.get(id=request.data["tacoProteinId_id"])
        shell = Shell.objects.get(id=request.data["tacoShellId_id"])
        new_my_built_taco = MyBuiltTaco.objects.create(
            name=request.data["name"],
            tacoLoverId=user,
            tacoProteinId=protein,
            tacoShellId=shell
        )
        serializer = MyBuiltTacoSerializer(new_my_built_taco)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_my_built_taco = MyBuiltTaco.objects.get(pk=pk)
        
        editing_my_built_taco.tacoLoverId = request.data["tacoLoverId_id"]
        editing_my_built_taco.tacoProteinId = request.data["tacoProteinId_id"]
        editing_my_built_taco.tacoShellId = request.data["tacoShellId_id"]
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
    
class MyBuiltTacoSerializer(serializers.ModelSerializer):
    """JSON serializer for mybuilttacos types"""
    class Meta:
        model = MyBuiltTaco
        fields = (
            'id',
            'tacoLoverId_id',
            'tacoProteinId_id',
            'tacoShellId_id',
            'name')