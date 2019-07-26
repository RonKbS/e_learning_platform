import json
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from e_l_p.schema import schema
from fixtures.user_fixtures import (
    user_mutation_query,
    user_mutation_response,
    user_query,
    user_query_response,
)
from fixtures.token_fixtures import user_token

class UserQueriesTestCase(TestCase):

    def setUp(self):
        self.client = Client()


    def test_a_user_can_be_created_and_returned(self):
        self._response = self.client.post(
            "/graphql/", json.dumps(user_mutation_query), content_type='application/json'
        )
        self.assertEqual(
            user_mutation_response,
            self._response.content
        )

    def test_users_can_be_queried(self):
        user = get_user_model()(
            username="test_user",
            email="test_user@gmail.com",
            is_superuser=True
        )
        user.set_password("testy1234")
        user.save()
        self._response = self.client.post(
            "/graphql/", json.dumps(user_query),
            content_type='application/json', HTTP_AUTHORIZATION="Token" + " " + user_token
        )
        self.assertEqual(
            user_query_response,
            self._response.content
        )
