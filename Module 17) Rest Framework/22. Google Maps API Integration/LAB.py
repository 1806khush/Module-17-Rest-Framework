# appointments/models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)  # Add address field
    
    latitude = models.FloatField(null=True, blank=True)  # Latitude field
    longitude = models.FloatField(null=True, blank=True)  # Longitude field
    
    def __str__(self):
        return self.name
# appointments/models.py
from geopy.geocoders import Nominatim
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Geocode the address
        if self.address:
            geolocator = Nominatim(user_agent="doctor_locator")
            location = geolocator.geocode(self.address)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super(Doctor, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
# appointments/views.py
from django.shortcuts import render
from .models import Doctor

def doctor_map(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctor_map.html', {'doctors': doctors})
