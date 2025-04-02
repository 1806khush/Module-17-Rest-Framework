# github_integration/views.py
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

def create_repository(request):
    """Create a new GitHub repository."""
    repo_name = request.GET.get('repo_name', '')
    if not repo_name:
        return JsonResponse({'error': 'Repository name is required'}, status=400)

    api_url = f'{GITHUB_API_URL}/user/repos'
    headers = {
        'Authorization': f'token {settings.GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'name': repo_name,
        'private': False,  # Set to True for private repository
    }

    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 201:
        return JsonResponse({'message': 'Repository created successfully', 'repository': response.json()})
    else:
        return JsonResponse({'error': response.json()}, status=response.status_code)


def list_user_repositories(request):
    """List all repositories for a given GitHub user."""
    username = request.GET.get('username', '')
    if not username:
        return JsonResponse({'error': 'Username is required'}, status=400)

    api_url = f'{GITHUB_API_URL}/users/{username}/repos'
    headers = {
        'Authorization': f'token {settings.GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        return JsonResponse({'repositories': repos})
    else:
        return JsonResponse({'error': response.json()}, status=response.status_code)
