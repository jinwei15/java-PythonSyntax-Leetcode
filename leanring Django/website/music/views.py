from django.shortcuts import render

# functions python
# take user request (web) and give back (web)/ logout/ download

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>this is a music app home </h1>")

def detail(request, album_id):
    return  HttpResponse("<h2> Details for Album id:" + str(album_id) +  "</h2>")