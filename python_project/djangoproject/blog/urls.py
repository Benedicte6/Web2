from django.contrib import admin
from django.urls import path


from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.home),
    path('post/<int:post_id>/', views.blog_post_view, name='post_view'),
    
]