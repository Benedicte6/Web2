from django.contrib import admin

# Register your models here.
from .models import *
# register each model with the admin site
admin.site.register(Produits)
admin.site.register(Event)
admin.site.register(Article)
admin.site.register(Agronome)
admin.site.register(Comment)
admin.site.register(Vote)