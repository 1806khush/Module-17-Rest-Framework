# models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# serializers.py
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact_details']
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorList(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()  # Retrieve all doctors from the database
        serializer = DoctorSerializer(doctors, many=True)  # Serialize the QuerySet
        return Response(serializer.data, status=status.HTTP_200_OK)
[
    {
        "id": 1,
        "name": "Dr. John Doe",
        "specialty": "Cardiology",
        "contact_details": "555-1234"
    },
    {
        "id": 2,
        "name": "Dr. Jane Smith",
        "specialty": "Neurology",
        "contact_details": "555-5678"
    }
]
