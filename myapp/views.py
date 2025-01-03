from django.shortcuts import render
from .models import About, Portfolio, Blog

def index(request):
    about_content = About.objects.first()
    portfolio = Portfolio.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'index.html', {
        'about_content': about_content,
        'portfolio': portfolio,
        'blogs': blogs
    })
