from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class Artist(models.Model):
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='artists')
    user = models.ForeignKey(User, related_name='artists', on_delete=models.DO_NOTHING)


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='songs')
    year = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='songs', on_delete=models.DO_NOTHING)


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="albums", on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='albums')
    genre = models.CharField(max_length=50)
    year = models.DateField(auto_now=True)
    desc = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='albums', on_delete=models.DO_NOTHING)