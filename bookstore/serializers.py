from rest_framework import serializers

from bookstore.models import Book


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    username = serializers.CharField()


class BookSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    user = UserSerializer()
    title = serializers.CharField()
    author = serializers.CharField()
    year = serializers.IntegerField()

