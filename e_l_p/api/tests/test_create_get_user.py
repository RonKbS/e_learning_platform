import json
from django.test import TestCase
from graphene.test import Client

from e_l_p.schema import schema
from fixtures.user_fixture import (
    user_mutation_query,
    user_mutation_response,
    user_query,
    user_query_response,
)


class UserQueriesTestCase(TestCase):

    def setUp(self):
        self._client = Client(schema)


    def test_a_user_can_be_created_and_returned(self):
        self._response = self._client.execute(user_mutation_query)
        import pdb; pdb.set_trace()
        self.assertEqual(
            {"username": "test_user", "email": "test_user@gmail.com", "id": "1"},
            dict(self._response["data"]["createUser"]["user"])
        )

    def test_users_can_be_queried(self):
        self._client.execute(user_mutation_query)
        self._response = self._client.execute(user_query)
        self.assertEqual(
            "test_user",
            dict(self._response["data"]["users"][0])["username"]
        )
