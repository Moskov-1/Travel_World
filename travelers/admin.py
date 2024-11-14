from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Locations, DestinationImage

admin.site.register(Locations)
admin.site.register(DestinationImage)