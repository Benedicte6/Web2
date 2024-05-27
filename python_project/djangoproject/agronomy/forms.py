from django import forms
from .models import Produits
from .models import Article,Event

 
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produits
        fields = [ 'title', 'content','image', 'is_published','pub_date','author' ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','introduction','technical_info','practical_tips','testimonials','infographic','author','links','conclusion']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'




