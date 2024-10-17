
from django.test import TestCase

from .models import About


# Create your tests here.
class AboutModelUnitTestCase(TestCase):
    def setUp(self):
        self.about = About.objects.get(
            title='Lorem ipsum dolor sit amet',
            description='Lorem ipsum dolor sit amet ,corecteture adipscing elit',
            icon='settings'
        )

    def test_about_model(self):
         data = self.about
         self.assertEqual(data, About)
