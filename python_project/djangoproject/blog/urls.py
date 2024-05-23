from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.blog_post_view, name='post_view'),
    path('post/<int:post_id>/', views.blog_post_detail, name='post-detail'),
    path('post/add/', views.blog_post_add,name='post-add'),
    path('post/<int:post_id>/change/', views.blog_post_change, name='post-change'),
    path('post/<int:post_id>/delete/', views.blog_post_delete, name='post-delete'),
    path('post/<int:post_id>/publish/', views.blog_post_publish, name='post-publish'),


    path('articles/', views.article_list, name='article_list'),
    path('articles/add/', views.article_add, name='article_add'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('articles/<int:pk>/edit/', views.article_change, name='article_change'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),




    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/new/', views.create_event, name='create_event'),
    path('events/<int:pk>/update/', views.update_event, name='update_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),

]