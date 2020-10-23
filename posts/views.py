from django.shortcuts import render, HttpResponse
from .models import Post

def home(request):

    posts = Post.objects.order_by('published_date')

    context = {'posts': posts}

    return render(request, 'posts/home.html', context)

def post_details(request, post_id):
    context = {'post_id': post_id}
    return render(request, 'posts/posts_details.html', context)