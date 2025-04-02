# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorList(APIView):
    def get(self, request):
        # Get all doctor records
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new doctor
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetail(APIView):
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return None

    def get(self, request, pk):
        doctor = self.get_object(pk)
        if doctor is None:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = self.get_object(pk)
        if doctor is None:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = self.get_object(pk)
        if doctor is None:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
