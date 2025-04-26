from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        print("Serializer data:", data)  # Что приходит в сериализатор?
        user = authenticate(**data)
        print("Authenticated user:", user)  # Что вернул authenticate?
        if not user:
            raise serializers.ValidationError("Неверные учетные данные")
        return user