from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from drf_yasg import openapi
from api.models import Book, Author, Category, Reservation
from api.serializers import BookRetrieveSerializer,\
                            AuthorSerializer,\
                            CategorySerializer,\
                            UserSerializer,\
                            UserRegisterSerializer,\
                            ReservationSerializer,\
                            ReservationCreateSerializer, \
                            BookCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your views here.
class ListUsersView(APIView):
    """List all users"""
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class RegisterUserView(APIView):
    """Register a new user"""
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate authentication token and return the response
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, description="Book title", type=openapi.TYPE_STRING),
            openapi.Parameter('author__name', openapi.IN_QUERY, description="Book author name", type=openapi.TYPE_STRING),
            openapi.Parameter('category__name', openapi.IN_QUERY, description="Category", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        """List all books"""
        query_params = request.query_params
        books = Book.objects.all()

        for attr, value in query_params.items():
            filter_param = '{}__icontains'.format(attr)
            lookup = {filter_param: value}
            books = books.filter(**lookup)

        serializer = BookRetrieveSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new book"""
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailUpdateDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        """Get a book by id"""
        book = get_object_or_404(Book, pk=pk)
        serializer = BookCreateSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a book by id"""
        book = get_object_or_404(Book, pk=pk)

        # Using the BookCreateSerializer because i don't want to display the author and category id
        serializer = BookCreateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a book by id"""
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListAuthorsCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Author name", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        """Get all authors in a list"""
        title = request.query_params.get('name', None)
        authors = Author.objects.all()
        if title:
            authors = authors.filter(name__icontains=title)
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new author"""
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailUpdateDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        """Get an author by id"""
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update an author by id"""
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCategoryCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """Get all categories in a list"""
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Create a new category"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailUpdateDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        """Get a category by id"""
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a category by id"""
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a category by id"""
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListReservationView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """Get all reservations in a list"""
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationDetailUpdateView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


class ReservationListCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """Get all reservations in a list"""
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new reservation"""
        serializer = ReservationCreateSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data['book']
            if not book.is_available:
                return Response({'error': 'Book is not available'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                book.is_available = False
                book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)