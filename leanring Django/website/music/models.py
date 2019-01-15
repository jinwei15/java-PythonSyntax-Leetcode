from django.db import models

# how we are going to save our data

# Create your models here. make a class will create a column in the data base
class Album(models.Model):
    # will be a column in DB
    artist = models.CharField(max_length=250) # ID of 1
    album_title = models.CharField(max_length=500)  # ID of 2
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # whenever we lookthrough the db give detail infor

    #string representation of this object
    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) # song will be deleted if we delete the album
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

# everytime makemigration and migrate to the database