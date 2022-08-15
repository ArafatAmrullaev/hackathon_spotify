from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ArtistSerializer, SongSerializer, AlbumSerializer
from .models import Artist, Song, Album
from rest_framework.permissions import IsAuthenticated, IsAdminUser
class ArtistViewSet(ModelViewSet, GenericViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class SongViewSet(ModelViewSet, GenericViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class AlbumSerializer(ModelViewSet, GenericViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]



