from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
class TestCustomRenderer(TestCase):

    def setUp(self):
        super(TestCustomRenderer, self).setUp()

    @classmethod
    def setUpTestData(cls):
        super(TestCustomRenderer, cls).setUpTestData()

    def test_custom_renderer(self):
        unauthenticated_user_api_client = APIClient()
        response = unauthenticated_user_api_client.get(
            "/example_model/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)