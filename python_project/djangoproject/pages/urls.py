
from pages import views as page_views #NEW
from django.conf import settings # NEW
from django.conf.urls.static import static # NEW
from django.contrib import admin
from django.urls import path



urlpatterns = [
    
    path('', page_views.home), #NEW
    path('Trends/', page_views.Trends),
    path('best_pratices/', page_views.practices),
    path('new_technologies/',page_views.technologies),
    path('about/',page_views.about),
    path('key_events/',page_views.events),

    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # NEW

