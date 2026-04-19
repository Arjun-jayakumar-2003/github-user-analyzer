from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os

@api_view(['GET'])
def test_api(request, username):

    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Authorization" : f"token {token}"
    }
    url = f"https://api.github.com/users/{username}"
    try:

        response = requests.get(url, headers=headers)

        if response.status_code == 404:
            return Response({"error" : "Github User not found"}, status=404)

        if response.status_code != 200:
            return Response({"error" : "Github API error"}, status=response.status_code)
        
    except Exception:
        return Response({"error" : "Something went wrong"}, status=503)
    
    data = response.json()
    
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url, headers=headers)
    repos_data = repos_response.json()

    total_stars = sum(repo.get("stargazers_count" , 0) for repo in repos_data)

    language_count = {}

    for repo in repos_data:
        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang , 0) + 1
    
    top_language = max(language_count , key=language_count.get) if language_count else None
    
    repo_count = data.get("public_repos" , 0)


    processed_data = {
        "Username" : data.get("login"),
        "repo_count" : repo_count,
        "total_stars" : total_stars,
        "top_language" : top_language
    }
    return Response(processed_data , status=response.status_code)