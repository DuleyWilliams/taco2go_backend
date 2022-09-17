""" A module for handling Menu Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from taco2goapi.models.tacoLover import TacoLover
from taco2goapi.models.tacoLover import TacoLover
from django.contrib.auth.models import User

class TacoLoverView(ViewSet):
    """ My Built Tacos Viewset """
    
    def retrieve(self, request, pk):
        """ Handle a GET request for a built taco"""
        try:
            taco_lover = TacoLover.objects.get(pk=pk)
            serializer = TacoLoverSerializer(taco_lover)
            return Response(serializer.data)
        except TacoLover.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ Handle a GET request for all built tacos"""
        taco_lovers = TacoLover.objects.all()
        serializer = TacoLoverSerializer(taco_lovers, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """ Handle a POST request for a built taco """
        user = TacoLover.objects.get(user=request.auth.user)
        email = TacoLover.objects.get(email=request.auth.user)
        
        new_taco_lover = TacoLover.objects.create(
            profilePic=request.data["profilePic"],
            userCity=request.data["userCity"],
            email=email,
            userState=request.data["userState"],
            user_id=request.data["user"]
        )
        serializer = TacoLoverSerializer(new_taco_lover)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk):
        """ Handles a PUT request for a menu item """
        editing_taco_lover = TacoLover.objects.get(pk=pk)
        
        editing_taco_lover.tacoLoverId_id = request.data["tacoLoverId_id"]
        editing_taco_lover.profilePic = request.data["profilePic"]
        editing_taco_lover.userCity = request.data["userCity"]
        editing_taco_lover.email = request.data["email"]
        editing_taco_lover.userState = request.data["userState"]
        editing_taco_lover.user_id = request.data["user_id"]
        editing_taco_lover.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """ Handles a DELETE request for a menu item """
        try:
            taco_lover = TacoLover.objects.get(pk=pk)
            taco_lover.delete()
        except TacoLover.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class TacoLoverSerializer(serializers.ModelSerializer):
    """JSON serializer for TacoLovers types"""
    class Meta:
        model = TacoLover
        fields = (
            'id',
            'profilePic',
            'userCity',
            'email',
            'userState',
            'user_id')