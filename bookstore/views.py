import pydash
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookstore.models import User, Book, Review
from bookstore.serializers import BookSerializer


# Create your views here.

@api_view(["POST"])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    User.create_user(username, password)
    return Response(status=200)


# reading list page with all added books to read or read
@api_view(["GET"])
def list_all_books(request):
    # data = []
    # la un model carti
    all_books = Book.objects.all()
    # code without serialization
    # for book in all_books:
    #       data.append(
    #           dict(
    #               booktitle=book.title,
    #               id=book.id
    #           )
    #       )
    # With serialization
    data = BookSerializer(all_books, many=True).data
    return Response(status=200, data=data)


#def home(request):
#    return HttpResponse("My bookstore")


@api_view(['POST'])
def add_book(request):
    user_id = request.data.get('user_id')
    get_book = request.data.get('book')
    get_author = request.data.get('author')
    get_year = request.data.get('year')
    user = User.objects.get(id=user_id)
    my_new_book = Book(title=get_book, user=user, author=get_author, year=get_year)
    my_new_book.save()
    return HttpResponse("Book added", status=200)


@api_view(["POST"])
def create_review(request):
    book_id = request.data.get('book_id')
    make_review = request.data.get('review')
    #  Verification of book and review text existence
    if not book_id and not make_review:
        return Response(status=status.HTTP_418_IM_A_TEAPOT)  # :D
    book = Book.objects.get(id=book_id)
    post_review = Review(text=make_review, book=book)
    post_review.save()
    return HttpResponse("Review added", status=200)


@api_view(["GET"])
def get_books(request, search_query):
    url = "https://getbooksinfo.p.rapidapi.com/"

    querystring = {"s": search_query}

    headers = {
        "X-RapidAPI-Key": "6fe88db82dmsh7ef124648db3c6dp1399e5jsn8bc2bf5ef176",
        "X-RapidAPI-Host": "getbooksinfo.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    book_data = response.json()

#    title = book_data.get('title', {})
#    year = book_data.get('year', {})

#    response_data = {
#       "title": title,
#        "year": year,
#    }

    return Response(status=status.HTTP_200_OK, data=book_data)


"""
    if response.status_code == 200:
        data = response.json()

        return JsonResponse(data)
    else:
        return HttpResponseServerError("Unable to fetch book data.")"""


def home(request):
    return render(request, "home.html")