from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "polls"
urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants_search/', views.restaurant_search, name='restaurant_search'),
    path('geolocation/', views.geolocation, name='geolocation'),
    path('favorites/', views.favorites, name='favorites'),
    path('details/<str:place_id>/', views.details, name='details'),

    # Get user location
    path('get_location/', views.get_location, name='get_location'),

    # Get nearby places
    path('receive_places/', views.receive_places, name='receive_places'),

    # REST API Links
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
    path('get_favorite_place_ids/', views.get_favorite_place_ids, name='get_favorite_place_ids')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

