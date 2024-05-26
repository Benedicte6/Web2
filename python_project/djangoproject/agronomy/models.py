from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date



# Create your models here.

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)


User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Assurez-vous d'importer User si vous n'avez pas déjà fait
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('agronomy.Article', on_delete=models.CASCADE)  # Assurez-vous d'importer Article si nécessaire

    def __str__(self):
        return f'Comment by {self.author.username} on {self.article.title}'
    

class Produits(models.Model):
    class Meta:
        permissions = [
            ("publish_product", "Can publish a Product")
        ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(unique=True, max_length=255)
    image = models.ImageField(upload_to="produit_images", null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.title + ("*" if self.is_published else "") 

    def get_absolute_url(self):
        return "/agronomy/produit/" + str(self.id) + "/"

  
class Event(models.Model):
    title = models.CharField(max_length=255, default='Untitled Event')
    description = models.TextField(default='')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date(2024, 12, 31))
    location = models.CharField(max_length=255, default='TBD')
    organizer = models.CharField(max_length=255, default='Unknown Organizer')
    contact_email = models.EmailField(default='default@example.com')
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def get_vote_count(self):
        return self.vote_set.count()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, default='Titre de l\'article')
    introduction = models.TextField(default='Introduction à l\'article...')
    technical_info = models.TextField(default='Informations techniques sur les techniques agricoles...')
    practical_tips = models.TextField(default='Conseils pratiques et recommandations pour les agriculteurs...')
    testimonials = models.TextField(default='Témoignages d\'agriculteurs ou d\'experts du secteur...')
    infographic = models.ImageField(upload_to='infographics/', default='images/default.png')
    links = models.URLField(default='http://www.example.com')
    conclusion = models.TextField(default='Conclusion de l\'article...')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Champ pour lier l'auteur de l'article

    def get_vote_count(self):
        return self.vote_set.count()
    def __str__(self):
        return self.title

class Agronome(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    specialisation = models.TextField(blank=True)
    def __str__(self):
        return self.name 

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

