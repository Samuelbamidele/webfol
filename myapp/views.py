from django.shortcuts import render
from .models import AboutMe, Portfolio, Blog

def index(request):
    about_me = AboutMe.objects.all()
    portfolio = Portfolio.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'index.html', {
        'about_me': about_me,
        'portfolio': portfolio,
        'blogs': blogs
    })
