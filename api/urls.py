from django.urls import path
from api.views import ListUsersView,\
                    ListBooksCreateView, \
                    ListAuthorsCreateView, \
                    ListCategoryCreateView, \
                    BookDetailUpdateDeleteView, \
                    AuthorDetailUpdateDeleteView, \
                    CategoryDetailUpdateDeleteView, \
                    ReservationListCreateView, \
                    ReservationDetailUpdateView, \
                    RegisterUserView

urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all"),
    path('users/register/', RegisterUserView.as_view(), name="users-register"),
    path('books/', ListBooksCreateView.as_view(), name="books-all"),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name="books-detail"),
    path('authors/', ListAuthorsCreateView.as_view(), name="authors-all"),
    path('authors/<int:pk>/', AuthorDetailUpdateDeleteView.as_view(), name="authors-detail"),
    path('categories/', ListCategoryCreateView.as_view(), name="categories-all"),
    path('categories/<int:pk>', CategoryDetailUpdateDeleteView.as_view(), name="categories-detail"),
    path('reservations/', ReservationListCreateView.as_view(), name="reservations-create"),
    path('reservations/<int:pk>', ReservationDetailUpdateView.as_view(), name="reservations-create"),

]
