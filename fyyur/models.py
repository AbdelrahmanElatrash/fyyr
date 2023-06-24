from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from datetime import datetime
from .genres import choices_geners ,check_genre
from multiselectfield import MultiSelectField       # pip install django-multiselectfield  , configure  'multiselectfield', in setting file 

    
class Venue(models.Model):
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=64)
    address=models.CharField(max_length=120)
    phone=models.CharField(max_length=64)
    img_link=models.URLField(null=True,blank=True)
    # img_link=models.CharField(max_length=500)
    facebook_link=models.URLField(null=True , blank=True)
    genres=MultiSelectField(choices=choices_geners,max_choices=30, max_length=120)
    website_link = models.URLField(null=True , blank=True)
    seeking_talent=models.BooleanField(default=True)
    seeking_description=models.TextField(null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    
    # show="realishin ship"

    def __str__(self):
        return self.name 

    def unique_cities(self):
        return Venue.objects.order_by().values('city').distinct()
    
    def get_absolute_url(self):
        return reverse('venue_list')
    
   
    
class Artist(models.Model):
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=64)
    phone=models.CharField(max_length=64)
    genres=MultiSelectField(choices=choices_geners,max_choices=30, max_length=120) 
    img_link=models.URLField(null=True,blank=True)
    facebook_link=models.URLField(null=True,blank=True)
    website_link=models.URLField(null=True,blank=True)
    seeking_venue=models.BooleanField(default=False)
    seeking_description=models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # show='relatioship'

    def __str__(self):
        return self.name +" id: " + str(self.id)
    
    def get_absolute_url(self):
        return reverse('artist_list')
    
class Show(models.Model):
    start_time=models.DateTimeField(null=False, blank=False)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='shows')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='shows')
    admin=models.ForeignKey(CustomUser,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        # return self.start_time
        return f"Show at {self.venue.name} featuring {self.artist.name}"
    
    def get_absolute_url(self):
        return reverse('show_list')


