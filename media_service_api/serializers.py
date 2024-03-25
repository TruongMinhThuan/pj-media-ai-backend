from rest_framework import serializers
from drf_yasg import openapi

class RemoveBackgroundRequestSerializer(serializers.Serializer):
    
    image_file = serializers.ImageField()
    
   