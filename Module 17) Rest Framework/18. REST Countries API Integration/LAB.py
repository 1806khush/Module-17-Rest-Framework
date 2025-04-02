# country_fetcher/views.py
import requests
from django.shortcuts import render

# The base URL for the REST Countries API
REST_COUNTRIES_API_URL = "https://restcountries.com/v3.1/name/"

def get_country_details(request):
    """Fetch details for a specific country."""
    country_name = request.GET.get('country', '').strip()
    
    if not country_name:
        return render(request, 'country_fetcher/index.html', {'error': 'Please enter a country name.'})
    
    # Make a request to the REST Countries API to get the country data
    response = requests.get(f'{REST_COUNTRIES_API_URL}{country_name}')
    
    if response.status_code == 200:
        country_data = response.json()[0]
        country_details = {
            'name': country_data.get('name', {}).get('common', 'N/A'),
            'population': country_data.get('population', 'N/A'),
            'languages': ', '.join(country_data.get('languages', {}).values()) if 'languages' in country_data else 'N/A',
            'currency': ', '.join(country_data.get('currencies', {}).keys()) if 'currencies' in country_data else 'N/A',
            'flag': country_data.get('flags', {}).get('png', 'N/A')
        }
        return render(request, 'country_fetcher/index.html', {'country': country_details})
    
    else:
        return render(request, 'country_fetcher/index.html', {'error': 'Country not found or API request failed.'})

