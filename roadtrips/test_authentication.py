from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'testUsername',
            'email@example.com',
            'testPassword'
            )

    def test_username_case_sensitivity(self):
        # This should return a User object because it's the exact username
        self.assertIsNotNone(authenticate(
            username='testUsername',
            password='testPassword'
        ))

        # Test should return None, proving active case-sensitivity
        self.assertIsNone(authenticate(
            username='testusername',
            password='testPassword'
        ))

    def test_password_case_sensitivity(self):
        # Test should return a User object because it's the exact password
        self.assertIsNotNone(authenticate(
            username='testUsername',
            password='testPassword'
        ))

        # Test should return None, proving active case-sensitivity
        self.assertIsNone(authenticate(
            username='testUsername',
            password='testpassword'
        ))
