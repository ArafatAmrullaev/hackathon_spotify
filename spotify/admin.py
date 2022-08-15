from django.contrib import admin

from .models import Artist, Song, Album, Comment, Rating, Like
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)


