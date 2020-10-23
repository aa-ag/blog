from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):

    posts = Post.objects.order_by('published_date')

    context = {'posts': posts}

    return render(request, 'posts/home.html', context)

def post_details(request, post_id):

    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)

    context = {'post': post}
    return render(request, 'posts/posts_details.html', context)