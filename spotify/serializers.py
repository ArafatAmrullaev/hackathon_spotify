from dataclasses import fields
from rest_framework import serializers
from .models import Artist, Song, Album


class ArtistSerializer(serializers):
    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(serializers):
    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers):
    class Meta:
        model = Album
        fields = '__all__'