# geocoding/views.py
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def geocode_address(request):
    address = request.GET.get('address', '')  # Get address from the query parameter
    if not address:
        return JsonResponse({'error': 'Address is required'}, status=400)

    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"

    # Make the request to the Google Maps API
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return JsonResponse({
            'address': address,
            'latitude': latitude,
            'longitude': longitude,
        })
    else:
        return JsonResponse({'error': 'Unable to geocode the address'}, status=400)
