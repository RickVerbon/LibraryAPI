from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    pages = models.IntegerField()
    isbn = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='books')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='reservations')
    reservation_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book.title
