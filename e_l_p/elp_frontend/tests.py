from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from fixtures.token_fixtures import user_token

class UserQueriesTestCase(TestCase):

    def setUp(self):
        self.client = Client()


    def test_use_of_signup_template(self):
        self._response = self.client.post(reverse('signup'))
        self.assertTemplateUsed(self._response, 'signup.html')

    def test_use_of_login_template(self):
        self._response = self.client.post(reverse('login'))
        self.assertTemplateUsed(self._response, 'registration/login.html')
