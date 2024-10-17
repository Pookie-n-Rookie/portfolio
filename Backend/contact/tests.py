from django.test import TestCase
from .models import Contact


class ContactModelUnitTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            address='West Bengal, India',
            email='banerjeeswarnendu6@gmail.com',
            phone='123456789'
        )

    def test_contact_model(self):
        data = self.contact
        self.assertIsInstance(data, Contact)