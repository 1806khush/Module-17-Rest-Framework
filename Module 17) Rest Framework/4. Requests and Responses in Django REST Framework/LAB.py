# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorCreate(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new doctor to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created doctor data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # If validation fails
