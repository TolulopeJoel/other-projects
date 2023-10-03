from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('comments', views.CommentViewset, basename='comments')


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts-list'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='posts-detail'),
]

urlpatterns += router.urls
