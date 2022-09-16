""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import restaurant
from taco2goapi.models.myFavs import MyFavs
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.rating import Rating
from taco2goapi.models.restaurant import Restaurant
from django.contrib.auth.models import User

class MyFavsView(ViewSet):
    """ My Built Tacos Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a built taco"""
        try:
            my_favs = MyFavs.objects.get(pk=pk)
            serializer = MyFavsSerializer(my_built_taco)
            return Response(serializer.data)
        except MyFavs.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all built tacos"""
        all_my_favs = MyFavs.objects.all()
        serializer = MyFavsSerializer(all_my_favs, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a built taco """
        user = TacoLover.objects.get(user=request.auth.user)
        rating = Rating.objects.get(id=request.data["ratingId_id"])
        restaurant = Restaurant.objects.get(id=request.data["restaurantId_id"])
        new_my_favs = MyFavs.objects.create(
            tacoLoverId=user,
            restaurantId=restaurant,
            ratingId=rating
        )
        serializer = MyFavsSerializer(new_my_favs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_my_favs = MyFavs.objects.get(pk=pk)
        
        editing_my_favs.ratingId_id = request.data["ratingId_id"]
        editing_my_favs.restaurantId_id = request.data["restaurantId_id"]
        editing_my_favs.tacoLoverId_id = request.data["tacoLoverId_id"]
        editing_my_favs.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a menu item """
        try:
            my_favs = MyFavs.objects.get(pk=pk)
            my_favs.delete()
        except MyFavsDoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class MyFavsSerializer(serializers.ModelSerializer):
    """JSON serializer for myfavs types"""
    class Meta:
        model = MyFavs
        fields = (
            'id',
            'ratingId_id',
            'restaurantId_id',
            'tacoLoverId_id'
            )