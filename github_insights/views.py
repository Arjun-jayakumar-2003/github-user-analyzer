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
    response = requests.get(url, headers=headers)
    data = response.json()

    return Response(data, status=response.status_code)