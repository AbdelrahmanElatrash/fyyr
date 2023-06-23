from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from datetime import datetime
from .genres import choices_geners ,check_genre
from multiselectfield import MultiSelectField       # pip install django-multiselectfield  , configure  'multiselectfield', in setting file 

# Create your models here.

# class Genre(models.Model):
#     name = models.CharField(max_length=100,choices=choices)

#     def __str__(self):
#         return self.name
    

class Venue(models.Model):
    name=models.CharField(max_length=64)
    city=models.CharField(max_length=64)
    address=models.CharField(max_length=64)
    phone=models.CharField(max_length=64)
    img_link=models.URLField(null=True)
    # genres=models.ManyToManyField(Genre)
    genres=MultiSelectField(choices=choices_geners,max_choices=30, max_length=120)
    seeking_talent=models.BooleanField(default=True)
    seeking_description=models.TextField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    facebook_link=models.URLField(null=True)
    # show="realishin ship"

    # def __str__(self):
    #     return self.name

    def unique_cities(self):
        return Venue.objects.order_by().values('city').distinct()
    
    def get_absolute_url(self):
        return reverse('venue_list')
    
    

class Artist(models.Model):
    name=models.CharField(max_length=64)
    city=models.CharField(max_length=64)
    phone=models.CharField(max_length=64)
    genres=MultiSelectField(choices=choices_geners,max_choices=30, max_length=120) 
    img_link=models.URLField(null=True)
    facebook_link=models.URLField(null=True)
    website_link=models.URLField(null=True)
    seeking_venue=models.BooleanField(default=False)
    seeking_description=models.TextField(null=True)
    # show='relatioship'

    def get_absolute_url(self):
        return reverse('artist_list')
    

class Show(models.Model):
    start_time=models.DateTimeField(null=False, blank=False)
    artist_id=models.ManyToManyField(Artist,related_name='shows')
    venue_id=models.ManyToManyField(Venue,related_name='shows')
    admin=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('show_list')


