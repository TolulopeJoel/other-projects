from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'bio',
            'profile_picture',
        ]


class RegisterUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(required=True)
    bio = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'bio',
            'username',
            'password',
            'password2'
        ]

    def create(self, validated_data):
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Passwords must match')
        return attrs


class PostPublicSerailizer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(read_only=True)
    body = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    status = serializers.CharField(read_only=True)


class ProfileSerailizer(serializers.ModelSerializer):
    published_articles_count = serializers.SerializerMethodField()
    draft_articles_count = serializers.SerializerMethodField()
    posts = PostPublicSerailizer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'gender',
            'bio',
            'profile_picture',
            'published_articles_count',
            'draft_articles_count',
            'date_joined',
            'posts',
        ]

    def get_draft_articles_count(self, obj):
        posts = obj.posts.all()
        count = len([post for post in posts if post.status == 'draft'])
        return count

    def get_published_articles_count(self, obj):
        posts = obj.posts.all()
        count = len([post for post in posts if post.status == 'published'])
        return count
