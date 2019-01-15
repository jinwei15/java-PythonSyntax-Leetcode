from django.urls import path,re_path
from .import views

# look at what URL is and
urlpatterns = [

    #mach , feedback
    path('', views.index, name='index'),

    #/music/71/ (ID of album)
    #name what the function is called.
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]
