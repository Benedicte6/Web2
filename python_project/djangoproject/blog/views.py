from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import*
from blog.forms import BlogPostForm
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
def home(request):
    posts = (BlogPost.objects
                .filter(is_published=True)
                .order_by('-pub_date')[:10]
)

# only published posts
# We pass the set of posts to the template

    data = {
    'blog_posts': posts
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
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect(blog_post)    # redirects to blog_post.get_absolute_url()
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog-post-add.html', { 'form': form })

@permission_required('blog.change_blogpost', raise_exception=True)
def blog_post_change(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id) # Need to fetch the specific object
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=blog_post)
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
