from django.contrib import admin
from .models import Show ,Venue ,Artist
# Register your models here.
class CustomShowAdmin(admin.ModelAdmin):
    model = Show
    

admin.site.register(Show, CustomShowAdmin)
admin.site.register(Venue)
admin.site.register(Artist)
