from django.utils.text import slugify
from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'body',
            'post',
            'created_at',
            'updated_at',
        ]


class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    body = serializers.CharField(write_only=True, required=True)
    summary_body = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'slug',
            'body',
            'summary_body',
            'thumbnail',
            'status',
        ]

    def get_summary_body(self, obj):
        post_body = (obj.body).split()
        return ' '.join(post_body[:33]) + '...'


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'body',
            'thumbnail',
            'published_date',
            'comments',
        ]
