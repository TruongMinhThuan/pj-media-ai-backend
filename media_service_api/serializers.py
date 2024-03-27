from rest_framework import serializers
from drf_yasg import openapi


class RemoveBackgroundRequestSerializer(serializers.Serializer):

    image_file = serializers.ImageField()


class RemoveBackgroundResponseSerializer(serializers.Serializer):

    input_image_url = serializers.CharField()
    processed_image_url = serializers.CharField()

