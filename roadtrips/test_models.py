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
    # Common objects set up to be reused by all tests in this class.
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


# Testing the Comment model.
class CommentModelTest(TestCase):
    # Common objects set up to be reused by all tests in this class.
    def setUp(self):
        # Create a test user.
        self.user = User.objects.create_user(
            username='testuser',
            password='123456'
            )

        # Create a test category.
        self.category = Category.objects.create(name="Test Category")

        # Create a test post.
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            category=self.category,
            content="Test Content"
            )

    # Checks the creation of a comment instance.
    def test_comment_creation(self):
        # Create a new comment instance.
        comment = Comment.objects.create(
            post=self.post,
            name="Test Name",
            email="test@example.com",
            body="Test Comment"
            )
        self.assertEqual(str(comment), "Comment Test Comment by Test Name")

    # Checks the default approval status of a new comment.
    def test_comment_approval(self):
        # Create a new comment instance.
        comment = Comment.objects.create(
            post=self.post,
            name="Test Name",
            email="test@example.com",
            body="Test Comment"
            )
        # Confirm that the comment's approval status is False by default.
        self.assertFalse(comment.approved)
