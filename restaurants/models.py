from django.db import models
from location_field.models.spatial import LocationField

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    coordinates = LocationField(based_fields=['city'], zoom=7)
    logo = models.ImageField(upload_to='logos')
