from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='slavic', password='abc123')
        self.post = Post.objects.create(
            author=self.user, title='Blog title', body='Body content...'
        )
        self.post.save()

    def test_blog_content(self):
        self.assertEqual(f"{self.post.author}", 'slavic')
        self.assertEqual(f"{self.post.title}", 'Blog title')
        self.assertEqual(f"{self.post.body}", 'Body content...')