from django.contrib import admin
from django.urls import path

from . import views

app_name = 'agronomy'
urlpatterns = [
    path('', views.home, name='home'),
    path('produit/<int:produit_id>/', views.produit_view, name='produit_view'),
    path('produit/<int:produit_id>/', views.produit_detail, name='produit_detail'),
    path('produit/add/', views.produit_add,name='produit_add'),
    path('produit/<int:produit_id>/change/', views.produit_change, name='produit_change'),
    path('produit/<int:produit_id>/delete/', views.produit_delete, name='produit_delete'),
    path('produit/<int:produit_id>/publish/', views.produit_publish, name='produit_publish'),


    path('articles/', views.article_list, name='article_list'),
    path('articles/add/', views.article_add, name='article_add'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('articles/<int:pk>/edit/', views.article_change, name='article_change'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),


    path('vote/article/<int:article_id>/', views.vote, name='vote_article'),
    path('vote/event/<int:event_id>/', views.vote, name='vote_event'),
    path('event/<int:event_id>/', views.event_view, name='view_event'),

    path('upload-article/', views.upload_article, name='upload_article'),
    path('upload-event/', views.upload_event, name='upload_event'),


    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/new/', views.create_event, name='create_event'),
    path('events/<int:pk>/update/', views.update_event, name='update_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),


]