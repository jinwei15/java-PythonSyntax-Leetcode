from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader
# functions python
# take user request (web) and give back (web)/ logout/ download

# Create your views here.


# def index(request):
#     return HttpResponse("<h1>this is a music app home </h1>")


def index(request):
    all_albums = Album.objects.all()
    html = ''

    for album in all_albums:
        url = 'music/' + str(album.id) + '/'
        html += '<a href="'+ url +'">' + album.album_title +'</a><br>'
    return HttpResponse(html)


def detail(request, album_id):
    return  HttpResponse("<h2> Details for Album id:" + str(album_id) +  "</h2>")