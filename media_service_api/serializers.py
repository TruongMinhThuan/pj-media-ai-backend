from rest_framework import serializers
from drf_yasg import openapi

class RemoveBackgroundRequestSerializer(serializers.Serializer):
    
    image_file = serializers.ImageField()
    
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "Email",
            "properties": {
                "subject": openapi.Schema(
                    title="Email subject",
                    type=openapi.TYPE_STRING,
                ),
                "body": openapi.Schema(
                    title="Email body",
                    type=openapi.TYPE_STRING,
                ),
                "attachment": openapi.Schema(
                    title="Email attachment",
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_BINARY,
                ),
                "image_file": openapi.Schema(
                    title="Image file",
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_BINARY,
                ),
            },
            "required": ["subject", "body"],
         }
