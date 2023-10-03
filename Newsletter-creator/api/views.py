from rest_framework import mixins, viewsets
from rest_framework import permissions

from .serializers import (
    PostSerializer,
    SubscriberSerializer,
)
from news.models import Post
from subscribers.models import Subscriber


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published', validated=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class SubscriberViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
