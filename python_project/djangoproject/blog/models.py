from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)


class Event(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    pub_date = models.DateField(null=True, blank=True)


class Article(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    pub_date = models.DateField(null=True, blank=True)

class Agronome(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    specialisation = models.TextField(blank=True)
    pub_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name