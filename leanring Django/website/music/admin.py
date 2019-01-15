from django.contrib import admin
# add model db into the admin UI
from .models import Album
# Register your models here.

# admin functionaility

admin.site.register(Album)