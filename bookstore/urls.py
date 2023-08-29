from django.urls import path

from bookstore import views
from bookstore.views import register_user, list_all_books, create_review

urlpatterns = [
    path("", views.home, name="home"),
    path("add-book/", views.add_book, name="add-book"),
    path("search-book/<search_query>", views.get_books),
    path("register/", register_user),
    path("book-list/", list_all_books),
    path("review_book/", create_review)
]
