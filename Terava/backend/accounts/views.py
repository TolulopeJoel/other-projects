from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterUserSerializer, ProfileSerailizer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerailizer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return super().get_queryset().filter(username=user.username, *args, **kwargs)
