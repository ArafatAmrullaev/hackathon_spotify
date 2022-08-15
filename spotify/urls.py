from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ArtistViewSet, SongViewSet, AlbumViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet)
router2 = DefaultRouter()
router2.register('songs', SongViewSet)
router3 = DefaultRouter()
router3.register('albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls))
]