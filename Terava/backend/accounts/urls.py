from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('profile', views.UserProfileViewset, basename='profile')


urlpatterns = [
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
]

urlpatterns += router.urls
