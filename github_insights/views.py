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

    return Response(data, status=response.status_code)