from django.shortcuts import render
from blog.data import posts

def blog(request):
    context = {
        # 'text': 'Olá Blog',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    context = {
        'text': 'Olá Exemplo'
    }
    return render(
        request,
        'blog/exemplo.html',
        context
    )

def post(request, id):
    print('post', id)
    context = {
        # 'text': 'Olá Blog',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )