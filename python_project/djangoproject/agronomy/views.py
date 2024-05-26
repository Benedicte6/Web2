from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from agronomy.models import*
from .forms import ProduitForm, ArticleForm
from .models import Article
from django.contrib.auth.decorators import permission_required, login_required
from .models import Event
from .forms import EventForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages

from .models import Article, Event, Comment
from django.http import HttpResponse

from .models import Vote

def vote(request, article_id=None, event_id=None):
    if request.method == 'POST':
        if article_id:
            existing_vote = Vote.objects.filter(user=request.user, article__isnull=False).exists()
            if not existing_vote:
                Vote.objects.create(user=request.user, article_id=article_id)
                messages.success(request, 'Votre vote pour l\'article a été enregistré avec succès!')
            else:
                messages.error(request, 'Vous avez déjà voté pour un article!')
            return redirect('agronomy:article_list')
        elif event_id:
            existing_vote = Vote.objects.filter(user=request.user, event__isnull=False).exists()
            if not existing_vote:
                Vote.objects.create(user=request.user, event_id=event_id)
                messages.success(request, 'Votre vote pour l\'événement a été enregistré avec succès!')
            else:
                messages.error(request, 'Vous avez déjà voté pour un événement!')
            return redirect('agronomy:event_list')
    return redirect('agronomy:home')
@receiver(post_save, sender=Article)
@receiver(post_save, sender=Event)
@receiver(post_save, sender=Comment)

def create_notification(sender, instance, created, **kwargs):
    if created:
        request = kwargs.get('request')
        if request:
            messages.info(request, f'New {sender.__name__} created: {instance.title}')
    return HttpResponse("Notification created successfully")

def home(request):
    produits = (Produits.objects
                .filter(is_published=True)
                .order_by('-pub_date')[:10])
    
    data = {
        'produits': produits,
        
        
    }
    
    return render(request, 'agronomy/home.html', data)


def produit_view(request, produit_id):
    produit = Produits.objects.get(id=produit_id)
    data = {
    'produit': produit
    }
    return render(request, 'agronomy/produit_view.html', data)


def produit_detail(request, produit_id):
    produit = get_object_or_404(Produits, id=produit_id)
    data = {
        'produit': produit
    }
    return render(request, 'agronomy/produit_detail.html', data)


@login_required
@permission_required('agronomy:add_produit', raise_exception=True)
def produit_add(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            blog_post = form.save()
            return redirect(blog_post)    # redirects to blog_post.get_absolute_url()
    else:
        form = ProduitForm()
    return render(request, 'agronomy/produit_add.html', { 'form': form })

@permission_required('agronomy.change_produit', raise_exception=True)
def produit_change(request, produit_id):
    produit = get_object_or_404(Produits, id=produit_id) # Need to fetch the specific object
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            produit = form.save() # This will update the object
            return redirect('/agronomy/')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'agronomy/produit_change.html', { 'form': form, 'produit': produit })

@permission_required('agronomy.delete_produit', raise_exception=True)
def produit_delete(request, produit_id):
    produit= get_object_or_404(Produits, id=produit_id)
    if request.method == "POST":
        produit.delete()
        return redirect('/agronomy/')
    return render(request, 'agronomy/produit_delete.html', { 'produit': produit })


def produit_publish(request, produit_id):
    produit = get_object_or_404(Produits, id=produit_id)
    if request.method == "POST":
        produit.is_published = True
        produit.pub_date = datetime.now()
        produit.save()
# Redirect to the post's detail page
    return redirect(produit)


def event_list(request):
    events = Event.objects.all()
    return render(request, 'agronomy/event_list.html', {'events': events})

def event_view(request, event_id):
    event = Event.objects.get(id=event_id)
    data = {
    'event': event
    }
    return render(request, 'agronomy/event_view.html', data)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event=form.save()
    else:
        form = EventForm(instance=event)
    
    return render(request, 'agronomy/event_detail.html', {'event': event, 'event_form': form})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agronomy:event_list')
    else:
        form = EventForm()
    return render(request, 'agronomy/event_form.html', {'form': form})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event=form.save()
            return redirect('agronomy:event_detail', pk=pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'agronomy/event_change.html', {'form': form, 'event':event})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('agronomy:event_list')
    return render(request, 'agronomy/event_confirm_delete.html', {'event': event})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'agronomy/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article=form.save()
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'agronomy/article_detail.html', {'article': article, 'article_form': form})

@login_required
def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()  # Ne pas sauvegarder l'instance pour le moment
            article.author = request.user  # Associer l'auteur actuel
            article.save()  # Maintenant, sauvegarder l'instance avec l'auteur

            messages.success(request, 'Article added successfully')  # Ajout d'un message de succès
            return redirect('agronomy:article_list')

    else:
        form = ArticleForm()
    
    return render(request, 'agronomy/article_form.html', {'form': form})

def article_change(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article=form.save()
            return redirect('agronomy:article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'agronomy/article_change.html', {'form': form, 'article':article})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('agronomy:article_list')
    return render(request, 'agronomy/article_delete.html', {'article': article})


def upload_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agronomy:article_list')
    else:
        form = ArticleForm()
    return render(request, 'agronomy/upload_article.html', {'form': form})

def upload_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agronomy:event_list')
    else:
        form = EventForm()
    return render(request, 'agronomy/upload_event.html', {'form': form})