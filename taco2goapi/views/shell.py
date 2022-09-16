""" A module for handling Rating requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import Shell

class ShellView(ViewSet):
    """ Shell Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a sauce"""
        try:
            shell = Shell.objects.get(pk=pk)
            serializer = ShellSerializer(shell)
            return Response(serializer.data)
        except Shell.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all sauces"""
        shells = Shell.objects.all()
        serializer = ShellSerializer(shells, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a rating """
        # incoming_user = request.auth.user
        new_shell = Shell.objects.create(
            type=request.data["type"]
        )
        serializer = ShellSerializer(new_shell)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a sauce """
        editing_shell = Shell.objects.get(pk=pk)
        
        editing_shell.type = request.data["type"]
        editing_shell.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a sauce """
        try:
            shell = Shell.objects.get(pk=pk)
            shell.delete()
        except Shell.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ShellSerializer(serializers.ModelSerializer):
    """JSON serializer for sauce"""
    class Meta:
        model = Shell
        fields = (
            'id',
            'type',)