A small book management api tool with functions to:
- create a user
- add a book to user(for let's say reading purpose)
- list all books that a user has
- add a review to a book

There is a test_client_bookstore that should contain
different client functions(just  user creation for the
moment).

PY PROJECT FILES:
- Models: contains db models(user, book, review)
- Serializers: (Book and User)
- Tests: tests for endpoints healthcheck
- Urls: url patterns
- Views: Available api functions

Examples for easy query:
- Add book query(127.0.0.1:8000/add-book): {"user_id":"get id from db","book":"Lotr", "author":"Tolkien","year":"1965"}
- Book review query(127.0.0.1:8000/review_book): {"book_id":"get id from db","review":"Greatest Book!"}

Unfinished functionality(**path("search-book/<search_query>"), get_book** function):
- Populate only necessary fields on json query
- Select a book from a returned api call, and add it