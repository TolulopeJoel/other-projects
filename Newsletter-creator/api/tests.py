from django.test import TestCase
from django.contrib.auth import get_user_model

from news.models import Post, NewsLetter

class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
        )
        
        cls.post = Post.objects.create(
            source='post source url',
            title="Test title",
            content="Test body",
            image="Test thumbnail",
            status='published',
            validated=True,
        )
        
    def test_post_model(self):
        """
        Test if post contains right parameters
        """        
        self.assertEqual(self.post.source, "post source url")
        self.assertEqual(self.post.title, "Test title")
        self.assertEqual(self.post.content, "Test body")
        self.assertEqual(self.post.image, "Test thumbnail")
        self.assertEqual(self.post.status, "published")
        self.assertEqual(self.post.validated, True)

class NewsLetterModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
        )     
        
        cls.newsletter = NewsLetter.objects.create(
            title="Test title",
            ready=True,
            published=True,
        )
        
    def test_newsletter_model(self):
        """
        Test if newsletter contains right parameters
        """        
        self.assertEqual(self.newsletter.title, "Test title")
        self.assertEqual(self.newsletter.ready, True)
        self.assertEqual(self.newsletter.published, True)

