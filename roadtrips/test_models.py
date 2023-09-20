from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, Comment


# Testing the Category model.
class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")


# Testing the Post model.
class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='123456'
            )
        self.category = Category.objects.create(name="Test Category")

    # Check the creation of a post instance.
    def test_post_creation(self):
        post = Post.objects.create(
            title="Test Post",
            author=self.user, category=self.category,
            content="Test Content"
            )
        self.assertEqual(str(post), "Test Post | testuser")

    # Check if unique slug is created based on the posts title.
    def test_slug_creation(self):
        post = Post.objects.create(
            title="Test Post",
            author=self.user,
            category=self.category,
            content="Test Content"
            )
        # Assert that the slug is created correctly based on the title.
        self.assertEqual(post.slug, "test-post")
