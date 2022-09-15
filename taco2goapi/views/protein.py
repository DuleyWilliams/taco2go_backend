""" A module for handling Protein requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import Protein

class ProteinView(ViewSet):
    """ Protein Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a protein"""
        try:
            protein = Protein.objects.get(pk=pk)
            serializer = ProteinSerializer(protein)
            return Response(serializer.data)
        except Protein.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all proteins"""
        proteins = Protein.objects.all()
        serializer = ProteinSerializer(proteins, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a protein """
        # incoming_user = request.auth.user
        new_protein = Protein.objects.create(
            type=request.data["type"]
        )
        serializer = ProteinSerializer(new_protein)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a protein """
        editing_protein = Protein.objects.get(pk=pk)
        
        editing_protein.type = request.data["type"]
        editing_protein.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a protein """
        try:
            protein = Protein.objects.get(pk=pk)
            protein.delete()
        except Protein.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ProteinSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""
    class Meta:
        model = Protein
        fields = (
            'id',
            'type',)