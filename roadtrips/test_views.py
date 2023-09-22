from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
from .models import Post, get_default_category, Comment
from .views import (PostList, PostDetail, PostLike,
                    PostCreate, PostUpdate, PostDelete)


class PostViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpass'
        )
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            status=1,
            author=self.user
        )
        self.client.login(username='testuser', password='testpass')

    def test_post_list_view(self):
        response = self.client.get(reverse('roadtrips'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')

    def test_post_detail_view_get(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')

    def test_post_detail_view_post(self):
        form_data = {
            'name': 'Test Commenter',
            'email': 'commenter@test.com',
            'content': 'Test Comment Content'
        }
        response = self.client.post(reverse(
            'post_detail', args=[self.post.pk]), form_data)
        self.assertEqual(response.status_code, 200)

    def test_post_like_view(self):
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)

    def test_post_unlike_view(self):
        self.post.likes.add(self.user)
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())
        response = self.client.post(reverse('post_like', args=[self.post.slug]))
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())

    def test_post_create_view(self):
        form_data = {
            'title': 'New Post',
            'content': 'New Content',
            'status': 1,
            'author': self.user.id,
            'category': get_default_category()
        }

        response = self.client.post(reverse('post_create'), form_data)

        self.assertEqual(response.status_code, 302)

    def test_post_update_view(self):
        form_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'status': 1,
            'author': self.user.id,
            'category': get_default_category()
        }
        response = self.client.post(reverse(
            'post_update', args=[self.post.pk]), form_data)

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
