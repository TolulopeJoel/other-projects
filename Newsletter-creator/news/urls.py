from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.newsboard, name='newsboard'),
    path('metrics/', views.metrics, name='metrics'),
    
    # post
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/create/', views.CreatePost.as_view(), name='create_post'),
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    # news letter
    path('news-letter/', views.NewsLetterList.as_view(), name='letter_list'),
    path('news-letter/create/', views.CreateLetter.as_view(), name='create_letter'),
    path('news-letter/previous/', views.PreviousNewsLetterList.as_view(), name='previous_newsletters'),
    path('news-letter/draft/<str:slug>/', views.DraftNewsLetterDetail.as_view(), name='draft_letter_detail'),
    path('news-letter/<str:slug>/', views.PublishedNewsLetterDetail.as_view(), name='letter_detail'),
    path('send_newsletter/<int:pk>/', views.send_newsletter, name='send_newsletter'),
]
