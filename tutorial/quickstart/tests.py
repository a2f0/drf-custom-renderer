from django.test import TestCase
class TestCustomRenderer(TestCase):

    def setUp(self):
        super(TestCustomRenderer, self).setUp()

    @classmethod
    def setUpTestData(cls):
        super(TestCustomRenderer, cls).setUpTestData()

    def test_custom_renderer(self):
        print('test custom renderer')