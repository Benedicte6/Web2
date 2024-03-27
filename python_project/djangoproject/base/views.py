from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def home(request):
    return render(request, 'pages/home.html')

def Trends(request):
    return render(request, 'pages/Trends.html')

def practices(request):
    return render(request, 'pages/best_pratices.html')