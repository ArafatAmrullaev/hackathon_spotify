from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ArtistSerializer, SongSerializer, AlbumSerializer
from .models import Artist, Song, Album, Rating, Comment, Like
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly

class ArtistViewSet(ModelViewSet, GenericViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]


class SongViewSet(ModelViewSet, GenericViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminOrReadOnly]


class AlbumViewSet(ModelViewSet, GenericViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAdminOrReadOnly]


@api_view(['GET'])
def toggle_like(request, a_id):
    user = request.user
    album = get_object_or_404(Album, id=a_id)

    if Like.objects.filter(user=user, album=album).exists():
        Like.objects.filter(user=user, album=album).delete()
    else:
        Like.objects.create(user=user, album=album)

    return Response('Like toggled', 200)

@api_view(['POST'])
def add_rating(request, a_id):
    user = request.user
    album = get_object_or_404(Album, id=a_id)
    value = request.POST.get('value')

    if not user.is_authenticated:
        raise ValueError('authentication credentials are not provided')

    if not value:
        raise ValueError('value is required')
    
    if Rating.objects.filter(user=user, album=album).exists():
        rating = Rating.objects.get(user=user, album=album)
        rating.value = value
        rating.save()

    else:
        Rating.objects.create(user=user, album=album, value=value)

    return Response('rating created', 201)



