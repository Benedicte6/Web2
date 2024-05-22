from django import forms
from .models import BlogPost
from .models import Article,Event
 
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [ 'title', 'content','image', 'is_published','pub_date','author' ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','introduction','practical_tips','testimonials','infographic','links','conclusion']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


