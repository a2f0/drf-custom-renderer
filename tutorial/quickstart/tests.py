from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

import factory

class ExampleModelFactory(factory.django.DjangoModelFactory):
   
    class Meta:
        model = 'quickstart.ExampleModel'

class TestCustomRenderer(TestCase):

    def setUp(self):
        super(TestCustomRenderer, self).setUp()

    @classmethod
    def setUpTestData(cls):
        super(TestCustomRenderer, cls).setUpTestData()

    def test_custom_renderer_get(self):
        example = ExampleModelFactory()
        unauthenticated_user_api_client = APIClient()
        response = unauthenticated_user_api_client.get(
            "/example_model/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['flag'], False)

    def test_custom_renderer_post(self):
        example = ExampleModelFactory()
        unauthenticated_user_api_client = APIClient()
        payload = {
            "flag": True
        }
        response = unauthenticated_user_api_client.post(
            "/example_model/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)