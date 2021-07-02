from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)


def post(request):
    if request.method == "POST":
        category = request.POST['category']
        color = request.POST['color']
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        Lost_date = request.POST['Lost_date'] 
        location = request.POST['location']
        mainphoto = request.FILES['mainphoto']
        board = Board(category = category, author=author, mainphoto=mainphoto, title=title, content=content, color = color, location = location, Lost_date = Lost_date)
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'post.html')
    
def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})

