from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User_details
from .serial import UserSerial
from .forms import userforms,product_forms
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class main(generics.ListCreateAPIView):
    queryset=User_details.objects.all()
    serializer_class=UserSerial

class home(APIView):
    def get(self,request,format=None):
        data=User_details.objects.all()
        serial=UserSerial(data,many=True)
        return Response(serial.data)
        

