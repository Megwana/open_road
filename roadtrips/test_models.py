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
        # Confirm the slug is created correctly based on the title.
        self.assertEqual(post.slug, "test-post")

    # Check the functionality of counting likes on a post.
    def test_like_count(self):
        post = Post.objects.create(
            title="Test Post",
            author=self.user,
            category=self.category,
            content="Test Content"
            )
        post.likes.add(self.user)

        # Confirm the number of likes on the post is correct.
        self.assertEqual(post.number_of_likes(), 1)

    def test_duplicate_title_error(self):
        # Creating the first test post
        Post.objects.create(
            title="Test Post",
            author=self.user,
            category=self.category,
            content="Test Content"
            )

        # Attempt to create 2nd post with same title should raise an error
        with self.assertRaises(Exception):
            Post.objects.create(
                title="Test Post",
                author=self.user,
                category=self.category,
                content="Test Content"
                )
