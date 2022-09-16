""" A module for handling Rating requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import Rating

class RatingView(ViewSet):
    """ Rating Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a rating"""
        try:
            rating = Rating.objects.get(pk=pk)
            serializer = RatingSerializer(rating)
            return Response(serializer.data)
        except Rating.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all ratings"""
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a rating """
        # incoming_user = request.auth.user
        new_rating = Rating.objects.create(
            type=request.data["type"]
        )
        serializer = RatingSerializer(new_rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a rating """
        editing_rating = Rating.objects.get(pk=pk)
        
        editing_rating.type = request.data["type"]
        editing_rating.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a rating """
        try:
            rating = Rating.objects.get(pk=pk)
            rating.delete()
        except Rating.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""
    class Meta:
        model = Rating
        fields = (
            'id',
            'type',)