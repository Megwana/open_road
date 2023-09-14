from django.test import TestCase
from .forms import PostForm, CommentForm
from .models import Category, Post
from django.contrib.auth.models import User


class PostFormTest(TestCase):

    def test_post_form_valid_data(self):
        category = Category.objects.create(name="Sample Category")
        user = User.objects.create_user(username='testuser', password='123456')

        form = PostForm(data={
            'title': 'Test title',
            'author': user.id,
            'excerpt': 'Test excerpt',
            'category': category.id,  # Use the Category instance's ID
            'featured_image': 'some_image.jpg',
            'content': 'Test content',
        })

        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid())

    def test_post_form_missing_title(self):
        category = Category.objects.create(name="Sample Category")
        user = User.objects.create_user(username='testuser', password='123456')

        form = PostForm(data={
            'author': user.id,
            'excerpt': 'Test excerpt',
            'category': category.id,
            'featured_image': 'some_image.jpg',
            'content': 'Test content',
        })

        self.assertFalse(form.is_valid())
        # Ensure 'title' field is in form errors
        self.assertIn('title', form.errors)
