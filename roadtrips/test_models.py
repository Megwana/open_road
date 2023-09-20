from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, Comment


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")
