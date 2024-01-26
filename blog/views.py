from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):

    search = Post.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    contx ={
        'post': search,
        'title': 'Memoirs of a wanderer',
    }
    
    return render(request, 'peges/index.html', contx)

def apout(request):
    return render(request, 'peges/about.html')

