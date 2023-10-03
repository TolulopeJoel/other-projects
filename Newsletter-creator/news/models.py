from django.db import models
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published'),
    )
    
    source = models.URLField(blank=True)
    title = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.URLField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    validated = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    posts = models.ManyToManyField(Post)
    ready = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title