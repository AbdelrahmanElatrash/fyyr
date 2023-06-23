
from .models import Venue,Show , Artist
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# Create your views here.

class VenueListView(ListView):
    template_name='fyyur/venue_list.html'
    model = Venue
    context_object_name='venues'


    

class VenueDetailView(DetailView):
    template_name='fyyur/venue_detail.html'
    model=Venue
    

class VenueCreateView(CreateView):
    template_name='fyyur/create_venue.html'
    model=Venue
    fields='__all__'

class VenueUpdateView(UpdateView):
    template_name='fyyur/update_venue.html'
    model=Venue
    fields="__all__"
    success_url=reverse_lazy('venue_list')

class VenueDeleteView(DeleteView):
    template_name='fyyur/delete_venue.html'
    model=Venue
    success_url=reverse_lazy('venue_list')

#   -------------------------------------------------------
class ArtistListView(ListView):
    template_name='fyyur/artist_list.html'
    model=Artist
    context_object_name='artists'

class ArtistDetailView(DetailView):
    template_name='fyyur/artist_detail.html'
    model=Artist

class ArtistCreateView(CreateView):
    template_name='fyyur/create_artist.html'
    model=Artist
    fields='__all__'

class ArtistUpdateView(UpdateView):
    template_name='fyur/update_artist.html'
    model=Artist
    fields="__all__"
    success_url=reverse_lazy('artist_list')

class ArtistDeleteView(DeleteView):
    template_name='fyyur/delete_artist.html'
    model=Artist
    success_url=reverse_lazy('artist_list')


# ------------------------------------------------

class ShowListView(ListView):
    template_name='fyyur/show_list.html'
    model=Show
    context_object_name='shows'
    

class ShowCreateView(CreateView):
    template_name='fyyur/create_show.html'
    model=Show
    fields="__all__"

