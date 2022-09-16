""" A module for handling Rating requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import Sauce

class SauceView(ViewSet):
    """ Sauce Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a sauce"""
        try:
            sauce = Sauce.objects.get(pk=pk)
            serializer = SauceSerializer(sauce)
            return Response(serializer.data)
        except Sauce.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all sauces"""
        sauces = Sauce.objects.all()
        serializer = SauceSerializer(sauces, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a rating """
        # incoming_user = request.auth.user
        new_sauce = Sauce.objects.create(
            type=request.data["type"]
        )
        serializer = SauceSerializer(new_sauce)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a sauce """
        editing_sauce = Sauce.objects.get(pk=pk)
        
        editing_sauce.type = request.data["type"]
        editing_sauce.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a sauce """
        try:
            sauce = Sauce.objects.get(pk=pk)
            sauce.delete()
        except Sauce.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class SauceSerializer(serializers.ModelSerializer):
    """JSON serializer for sauce"""
    class Meta:
        model = Sauce
        fields = (
            'id',
            'type',)