
from pages import views as page_views #NEW
from django.contrib import admin
from django.urls import path

app_name = 'pages'

urlpatterns = [
    
    path('', page_views.home, name='home'), #NEW
    path('Trends/', page_views.Trends,name='Trends'),
    path('best_pratices/', page_views.practices,name='practices'),
    path('new_technologies/',page_views.technologies,name='technologies'),
    path('about/',page_views.about,name='about'),
    path('key_events/',page_views.events,name='events'),

    
]  
