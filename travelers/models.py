from django.db import models
from PIL import Image,  ImageDraw, ImageOps
import os
from django.conf import settings

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_image and hasattr(self.main_image, 'path'):
            img = Image.open(self.main_image.path)
            max_width = 310
            max_height = 355
            
            img.thumbnail((max_width, max_height), Image.LANCZOS)
            mask = Image.new("L", img.size, 0)
            draw = ImageDraw.Draw(mask)
            radius = 20
            draw.rounded_rectangle(
                (0, 0, img.size[0], img.size[1]),
                radius=radius,
                fill=255
            )
            rounded_img = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
            rounded_img.putalpha(mask)
            rounded_img.save(self.main_image.path,format="PNG")

            thumbnail_size = (200, 150)  # Example thumbnail size
            img.thumbnail(thumbnail_size, Image.LANCZOS)

            # Save the thumbnail to the thumbnail field
            # Define the thumbnail path
            thumbnail_dir = os.path.join(settings.MEDIA_ROOT, 'destinations/thumbnails/')
            os.makedirs(thumbnail_dir, exist_ok=True)  # Create the directory if it doesn't exist
            thumbnail_path = os.path.join(thumbnail_dir, os.path.basename(self.main_image.name))
            img.save(thumbnail_path)
            #super().save(update_fields=['rounded_image'])
class DestinationImage(models.Model):
    image = models.ImageField(upload_to='destination_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Image for {self.caption or 'destination'}"
class Package(models.Model):
    name = models.CharField(max_length=200)
