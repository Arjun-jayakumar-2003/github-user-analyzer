from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_api(request, username):
    return Response({"message" : f"Api is working! Hello {username}"})