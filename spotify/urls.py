from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ArtistViewSet, CommentViewSet, SongViewSet, AlbumViewSet, toggle_like, add_rating, add_to_favourite, FavouriteViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet)
router2 = DefaultRouter()
router2.register('songs', SongViewSet)
router3 = DefaultRouter()
router3.register('albums', AlbumViewSet)
router4 = DefaultRouter()
router4.register('favourites', FavouriteViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
    path('albums/toggle_like/<int:a_id>/', toggle_like),
    path('albums/add_rating/<int:a_id>/', add_rating),
    path('song/add_to_favourite/<int:s_id>/', add_to_favourite),
    path('', include(router4.urls))
]