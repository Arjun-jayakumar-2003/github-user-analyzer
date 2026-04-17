from django.urls import path
from .views import test_api

urlpatterns = [
    path('test/<str:username>/' , test_api),
]