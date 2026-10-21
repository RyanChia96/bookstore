from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = ["id", "name"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ["id", "name"]