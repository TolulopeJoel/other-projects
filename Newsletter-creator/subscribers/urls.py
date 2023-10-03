from django.urls import path

from . import views

app_name = 'subscribers'

urlpatterns = [
    path('', views.add_subscriber, name='add'),
    path('confirm/<uidb64>/<token>/', views.confirm_subscriber, name='confirm'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('image_load/<uidb64>/<token>/', views.image_load, name='image_load'),
]