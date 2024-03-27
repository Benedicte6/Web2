from django.shortcuts import render

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

