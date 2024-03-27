
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def Trends(request):
    return render(request, 'pages/Trends.html')

def practices(request):
    return render(request, 'pages/best_pratices.html')

def technologies(request):
    return render(request, 'pages/new_technologies.html')

def about(request):
    return render(request, 'pages/about.html')

def events(request):
    return render(request, 'pages/key_events.html')
