from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post

def home(request):
    """
    Render a home page with all blog posts from latest to oldest.
    """
    posts = Post.objects.order_by('-published_date')

    context = {'posts': posts}

    return render(request, 'posts/home.html', context)


def post_details(request, post_id):
    """
    Redirect user to entire post to show post details
    """
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)

    context = {'post': post}
    return render(request, 'posts/posts_details.html', context)


def search(request):
    """
    Route to enable search bar / searching posts by titles / keywords
    """
    if request.method == 'GET':
        search = request.GET.get('search')
        result = Post.objects.all().filter(title__icontains=search)
        if result:
            context = {'result':result}
            return render(request, 'posts/results.html', context)
        else:
            return HttpResponse("<h3>Go back! Result not found... 🕺</h3>")