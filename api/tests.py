from django.test import TestCase
from api.models import Book, Author, Category
from django.contrib.auth.models import User


# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Fantasy")

    def test_if_category_is_created(self):
        category = Category.objects.get(name="Fantasy")
        self.assertEqual(category.name, 'Fantasy')

    def test_if_category_is_updated(self):
        category = Category.objects.get(name="Fantasy")
        category.name = "Sci-Fi"
        category.save()
        updated_category = Category.objects.get(name="Sci-Fi")
        self.assertEqual(updated_category.name, "Sci-Fi")

    def test_if_category_is_deleted(self):
        category = Category.objects.get(name="Fantasy")
        category.delete()
        deleted_category = Category.objects.filter(name="Fantasy")
        self.assertEqual(deleted_category.count(), 0)


class AuthorTestCase(TestCase):
    def setUp(self):
        author = Author.objects.create(name="J. R. R. Tolkien",
                                       gender="male",
                                       country="United Kingdom")

    def test_if_author_is_created(self):
        author = Author.objects.get(name='J. R. R. Tolkien')
        self.assertEqual(author.name, 'J. R. R. Tolkien')

    def test_if_author_is_updated(self):
        author = Author.objects.get(name='J. R. R. Tolkien')
        author.name = "Dick Bruna"
        author.save()
        updated_author = Author.objects.get(name='Dick Bruna')
        self.assertEqual(updated_author.name, 'Dick Bruna')

    def test_if_author_is_deleted(self):
        author = Author.objects.get(name='J. R. R. Tolkien')
        author.delete()
        deleted_author = Author.objects.filter(name='J. R. R. Tolkien')
        self.assertEqual(deleted_author.count(), 0)


class BookTestCase(TestCase):
    def setUp(self):
        test_author = Author.objects.create(name="J. R. R. Tolkien",
                                            gender="male",
                                            country="United Kingdom")

        test_category = Category.objects.create(name='Fantasy')
        book = Book.objects.create(title='The Lord of the Rings',
                                   author=test_author,
                                   pages=1178,
                                   isbn='978-0-618-57498-5',
                                   language='English')
        book.category.set([test_category])

    def test_if_author_is_created(self):
        author = Author.objects.get(name='J. R. R. Tolkien')
        self.assertEqual(author.name, 'J. R. R. Tolkien')

    def test_if_category_is_created(self):
        category = Category.objects.get(name="Fantasy")
        self.assertEqual(category.name, 'Fantasy')

    def test_if_book_is_created(self):
        book = Book.objects.get(title='The Lord of the Rings')
        self.assertEqual(book.title, 'The Lord of the Rings')

    def test_book_has_category(self):
        book = Book.objects.get(title='The Lord of the Rings')
        category = Category.objects.get(name='Fantasy')
        self.assertEqual(book.category.first(), category)

    def test_book_has_author(self):
        book = Book.objects.get(title='The Lord of the Rings')
        author = Author.objects.get(name='J. R. R. Tolkien')
        self.assertEqual(book.author.name, author.name)

    def test_if_book_is_updated(self):
        book = Book.objects.get(title="The Lord of the Rings")
        book.title = "The Hobbit"
        book.save()
        updated_book = Book.objects.get(title="The Hobbit")
        self.assertEqual(updated_book.title, "The Hobbit")

    def test_if_book_is_deleted(self):
        book = Book.objects.get(title="The Lord of the Rings")
        book.delete()
        deleted_book = Book.objects.filter(title="The Lord of the Rings")
        self.assertEqual(deleted_book.count(), 0)


class UserTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='12345678')

    def test_if_user_is_created(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')

    def test_if_user_is_deleted(self):
        user = User.objects.get(username='testuser')
        user.delete()
        deleted_user = User.objects.filter(username='testuser')
        self.assertEqual(deleted_user.count(), 0)