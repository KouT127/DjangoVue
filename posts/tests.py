import json
from users.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Post
from .serializer import PostSerializer

class PostViewSetTestCase(APITestCase):

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create(username=self.username,email=self.email,password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.key)
    
    def test_create_post(self):
        self.setUp()
        url = reverse('posts')
        response = self.client.post(url, {"content": "Test!"})
        self.assertEqual(200, response.status_code)