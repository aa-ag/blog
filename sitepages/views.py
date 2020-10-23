from django.shortcuts import render, get_object_or_404, HttpResponse
import requests

def about(request):
    """
    Render about page
    """
    return render(request, 'about.html')

def by(request):
    """
    Render by page
    """
    return render(request, 'by.html')

def credentials(request):
    """
    Render credentials page consuming Codewars' API
    """

    data = requests.get('https://www.codewars.com/api/v1/users/aa-ag').json()

    username = data['username']
    honor = data['honor']
    clan = data['clan']
    rank = data['ranks']['overall']['name']
    total_completed = data['codeChallenges']['totalCompleted']

    context = {'username':username, 'honor':honor, 'clan':clan, 'rank':rank, 'total_completed':total_completed}
    return render(request, 'credentials.html', context)