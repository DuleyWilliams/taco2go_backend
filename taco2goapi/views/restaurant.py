""" A module for handling Restaurant requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models import Restaurant

class RestaurantView(ViewSet):
    """ Restaurant Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a restaurant"""
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all proteins"""
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a protein """
        # incoming_user = request.auth.user
        new_restaurant = Restaurant.objects.create(
            restaurantName=request.data["restaurantName"],
            address=request.data["address"],
            zipCode=request.data["zipCode"],
            phone=request.data["phone"],
            website=request.data["website"],
            email=request.data["email"],
            stateName=request.data["stateName"],
            cityName=request.data["cityName"],
            cuisineType=request.data["cuisineType"],
            hoursInterval=request.data["hoursInterval"]
        )
        serializer = RestaurantSerializer(new_restaurant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a restaurant """
        editing_restaurant = Restaurant.objects.get(pk=pk)
        
        editing_restaurant.restaurantName = request.data["restaurantName"]
        editing_restaurant.address = request.data["address"]
        editing_restaurant.zipCode = request.data["zipCode"]
        editing_restaurant.phone = request.data["phone"]
        editing_restaurant.website = request.data["website"]
        editing_restaurant.email = request.data["email"]
        editing_restaurant.stateName = request.data["stateName"]
        editing_restaurant.cityName = request.data["cityName"]
        editing_restaurant.cuisineType = request.data["cuisineType"]
        editing_restaurant.hoursInterval = request.data["hoursInterval"]
        editing_restaurant.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a protein """
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            restaurant.delete()
        except Restaurant.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class RestaurantSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""
    class Meta:
        model = Restaurant
        fields = (
            'id',
            'restaurantName',
            'address',
            'zipCode',
            'phone',
            'website',
            'email',
            'stateName',
            'cityName',
            'cuisineType',
            'hoursInterval',)