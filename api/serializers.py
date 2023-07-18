from rest_framework import serializers
from api.models import Book, Author, Category, Reservation
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
        fields = ('id', 'title', 'author', 'pages', 'isbn', 'language', 'category', "is_available")


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'pages', 'isbn', 'language', 'category', 'is_available')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff')


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, max_length=128, min_length=8)
    email = serializers.EmailField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class ReservationSerializer(serializers.ModelSerializer):
    reservation_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Reservation
        fields = ('id', 'book', 'user', 'reservation_date', 'return_date')


class ReservationCreateSerializer(serializers.ModelSerializer):
    reservation_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', required=False)

    class Meta:
        model = Reservation
        fields = ('id', 'book', 'user', 'reservation_date')
