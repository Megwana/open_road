from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Comment, Post


class AdminTests(TestCase):

    def setUp(self):
        # Create test admin user
        self.admin_user = User.objects.create_superuser(
            username='admin', password='testpass', email='admin@example.com'
        )
        self.client = Client()

        # Log in the test admin user
        self.client.login(username='admin', password='testpass')

        # Create a sample post
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            author=self.admin_user,
            status=1
        )

        # Create test comments that are not approved
        self.comments = [
            Comment.objects.create(
                post=self.post,
                name='Commenter',
                email='commenter@example.com',
                body=f'Comment {i}',
                approved=False)
            for i in range(3)
        ]

    def test_approve_comments_action(self):
        # URL for the change list view of comments in the admin
        url = reverse('admin:roadtrips_comment_changelist')

        # The IDs of the comments wanting approval
        data = {
            'action': 'approve_comments',
            '_selected_action': [comment.id for comment in self.comments],
        }
        response = self.client.post(url, data)

        # Ensure the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check all the comments are now approved
        for comment in self.comments:
            comment.refresh_from_db()  # Fetch latest data from DB
            self.assertTrue(comment.approved)
