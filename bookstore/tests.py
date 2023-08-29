from django.test import TestCase, Client

from bookstore.models import User


# Create your tests here.

class EndpointsTests(TestCase):

    def test_homepage_is_loading(self):
        client = Client()
        # call the endpoint
        response = client.get('')
        # verify if the endpoint is called successfully
        self.assertEquals(response.status_code, 200)

    def test_book_list_api(self):
        client = Client()
        # call the endpoint
        response = client.get('/bookstore/book-list/')
        # verify if the endpoint is called successfully and has no content
        self.assertEquals(response.status_code, 404)
