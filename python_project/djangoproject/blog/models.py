from django.db import models
from django.conf import settings

# Create your models here.

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)


User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    class Meta:
        permissions = [
            ("publish_blogpost", "Can publish a BlogPost")
        ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title + ("*" if self.is_published else "") 

    def get_absolute_url(self):
        return "/blog/post/" + str(self.id) + "/"



class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    pub_date = models.DateField(null=True, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    pub_date = models.DateField(null=True, blank=True)

class Agronome(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    specialisation = models.TextField(blank=True)
    pub_date = models.DateField(null=True, blank=True)
    


    
