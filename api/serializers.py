from rest_framework import serializers
from api.models import Book, Author, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'gender', 'country')


class BookRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'pages', 'isbn', 'language', 'category')


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'pages', 'isbn', 'language', 'category')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff')