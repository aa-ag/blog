from django.shortcuts import render, get_object_or_404, HttpResponse

def about(request):
    return render(request, 'about.html')

def by(request):
    return render(request, 'by.html')
