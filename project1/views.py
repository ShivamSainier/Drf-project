from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User_details
from .serial import UserSerial
from .forms import userforms,product_forms
from rest_framework.views import APIView

# Create your views here.

class main(generics.ListCreateAPIView):
    queryset=User_details.objects.all()
    serializer_class=UserSerial