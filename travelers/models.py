from django.db import models

# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True, null=True)
    attractions = models.JSONField(blank=True, null=True) 
    best_time_to_visit = models.JSONField(blank=True, null=True)
    main_image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    additional_images = models.ManyToManyField('DestinationImage', blank=True)    
    def __str__(self):
        return self.name

class DestinationImage(models.Model):
    image = models.ImageField(upload_to='destination_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Image for {self.caption or 'destination'}"
class Package(models.Model):
    name = models.CharField(max_length=200)
