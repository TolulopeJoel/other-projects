from rest_framework import serializers

from news.models import Post
from subscribers.models import Subscriber


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]
