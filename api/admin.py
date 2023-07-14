from django.contrib import admin
from api.models import Book, Author, Category

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
