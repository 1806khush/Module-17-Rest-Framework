# weather/views.py
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def get_weather(request):
    city = request.GET.get('city', 'London')  # Default to 'London' if no city is provided
    api_key = settings.OPENWEATHERMAP_API_KEY  # Store your API key in settings
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return JsonResponse(weather_info)  # Return the weather data in JSON format
    else:
        return JsonResponse({'error': 'City not found or API error'}, status=400)
