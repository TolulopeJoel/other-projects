from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published'),
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='media/post_thumbnail/%Y/%m/%d')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    published_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='comments',
        null=True
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)
