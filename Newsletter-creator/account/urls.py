from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
app_name = 'account'


urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    # path('register/', views.register_user, name='register'),
    # path('edit/', views.edit, name='edit'),
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('manage-posts/', views.post_manager, name='post_manager'),
    # path('delete-account/<int:pk>/', views.DeleteView.as_view(), name='delete_account'),
]
