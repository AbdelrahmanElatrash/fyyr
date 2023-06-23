from django.urls import path
from .views import *


urlpatterns = [
    path('venues/',VenueListView.as_view(),name='venue_list') ,
    path('venues/create/', VenueCreateView.as_view() , name='create_venue'),
    path('venues/<int:pk>/', VenueDetailView.as_view(), name='venue_detail'),
    path('venues/<int:pk>/update/',VenueUpdateView.as_view(),name='update_venue'),
    path('venues/<int:pk>/delete/', VenueDeleteView.as_view(), name='delete_venue'),

    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artists/create' , ArtistCreateView.as_view(),name='create_artist'),
    path('artist/<int:pk>/', ArtistDetailView.as_view() ,name='artist_detail'),
    path('rtist/<int:pk>/update/',ArtistUpdateView.as_view(),name='update_artist'),
    path('rtist/<int:pk>/delete/', ArtistDeleteView.as_view(), name='delete_artist'),

    path('shows', ShowListView.as_view(), name='show_list'),
    path('shows/create',ShowCreateView.as_view() , name='create_show'),
   
    
    
    
]