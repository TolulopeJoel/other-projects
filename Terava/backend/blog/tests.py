from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
        )
        
        cls.post = Post.objects.create(
            author=cls.user,
            title="Test title",
            body="Test body",
            thumbnail="Test thumbnail",
        )
        
    def test_post_model(self):
        """
        Test if post contains right parameters
        """        
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test title")
        self.assertEqual(self.post.body, "Test body")
        self.assertEqual(self.post.thumbnail, "Test thumbnail")
