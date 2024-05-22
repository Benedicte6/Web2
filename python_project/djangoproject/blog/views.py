from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import*
from .forms import BlogPostForm, ArticleForm
from .models import Article
from django.contrib.auth.decorators import permission_required, login_required
from .models import Event
from .forms import EventForm

# Create your views here.
def home(request):
    posts = (BlogPost.objects
                .filter(is_published=True)
                .order_by('-pub_date')[:10])
    #posts = BlogPost.objects.filter(is_published=True).order_by('-pub_date')[:10]
    articles = Article.objects.all()
    data = {
        'blog_posts': posts,
        'articles': articles,
        
    }
    
    return render(request, 'blog/home.html', data)


def blog_post_view(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)
    data = {
    'post': blog_post
    }
    return render(request, 'blog/blog-post-view.html', data)


def blog_post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    data = {
        'post': blog_post
    }
    return render(request, 'blog/blog-post-detail.html', data)


@login_required
@permission_required('blog:add_blogpost', raise_exception=True)
def blog_post_add(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            blog_post = form.save()
            return redirect(blog_post)    # redirects to blog_post.get_absolute_url()
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog-post-add.html', { 'form': form })

@permission_required('blog.change_blogpost', raise_exception=True)
def blog_post_change(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id) # Need to fetch the specific object
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            blog_post = form.save() # This will update the object
            return redirect('/blog/')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/blog-post-change.html', { 'form': form, 'post': blog_post })

@permission_required('blog.delete_blogpost', raise_exception=True)
def blog_post_delete(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        blog_post.delete()
        return redirect('/blog/')
    return render(request, 'blog/blog-post-delete.html', { 'post': blog_post })


def blog_post_publish(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        blog_post.is_published = True
        blog_post.pub_date = datetime.now()
        blog_post.save()
# Redirect to the post's detail page
    return redirect(blog_post)

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = ArticleForm()
    
    return render(request, 'blog/article_add.html', {'form': form})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

def article_change(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article=form.save()
            return redirect('blog:article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'blog/article_change.html', {'form': form, 'article': article})

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == "POST":
        article.delete()
        return redirect('blog:article_list')
    
    return render(request, 'blog/article_delete.html', {'article': article })

def event_list(request):
    events = Event.objects.all()
    return render(request, 'blog/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/event_detail.html', {'event': event})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:event_list')
    else:
        form = EventForm()
    return render(request, 'blog/event_form.html', {'form': form})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event=form.save()
            return redirect('blog:event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/event_change.html', {'form': form, 'event':event})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('blog:event_list')
    return render(request, 'blog/event_confirm_delete.html', {'event': event})