from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Oliver',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 8, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 8, 2022'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def projects(request):
    return render(request, 'blog/projects.html', {'title': 'Projects'})
    