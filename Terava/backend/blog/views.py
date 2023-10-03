import random

from django.contrib.auth import get_user_model
from django.utils.text import slugify

from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer, UserSerializer, CommentSerializer


def rand_slug():
    return random.randrange(1003, 9987)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostListSerializer

    def perform_create(self, serializer):
        author = self.request.user
        title = serializer.validated_data.get('title')
        slug = f'{author.username}-{rand_slug()}-' + slugify(title)
        return serializer.save(author=author, slug=slug)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        try:
            user = self.request.user
            post_id = self.request.data.get('post_id')
            post = Post.objects.get(id=post_id)
            return serializer.save(author=user, post=post)
        except:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
