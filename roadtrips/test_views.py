from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
from .views import (PostList, PostDetail, PostLike,
                    PostCreate, PostUpdate, PostDelete)


class PostViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
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
