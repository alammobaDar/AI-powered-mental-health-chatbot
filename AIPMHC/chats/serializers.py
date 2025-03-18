from rest_framework import serializers


class ChatSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)