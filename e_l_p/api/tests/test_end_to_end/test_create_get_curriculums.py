import json
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from e_l_p.schema import schema
from fixtures.course_fixtures import (
    curriculum_mutation_query,
    curriculum_mutation_response,
    curriculum_query,
    curriculum_query_response
)
from fixtures.token_fixtures import user_token


class CurriculumQueriesTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        user = get_user_model()(
            username="test_user",
            email="test_user@gmail.com",
            is_staff=True
        )
        user.set_password("testy1234")
        user.save()

    def test_a_curriculum_can_be_created_and_returned(self):
        self._response = self.client.post(
            "/graphql/", json.dumps(curriculum_mutation_query),
            content_type='application/json', HTTP_AUTHORIZATION="Token" + " " + user_token
        )
        self.assertEqual(
            curriculum_mutation_response,
            self._response.content
        )

        self._response = self.client.post(
            "/graphql/", json.dumps(curriculum_query),
            content_type='application/json', HTTP_AUTHORIZATION="Token" + " " + user_token
        )
        self.assertEqual(
            curriculum_query_response,
            self._response.content
        )
