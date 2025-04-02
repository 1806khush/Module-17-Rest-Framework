# doctor_finder/models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# doctor_finder/serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact_details']
# doctor_finder/views.py
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
