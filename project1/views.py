from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User_details,Products
from .serial import UserSerial,ProductSerial
from .forms import userforms,product_forms
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import requests
# Create your views here.

class main(generics.ListCreateAPIView):
    queryset=User_details.objects.all()
    serializer_class=UserSerial

class create(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerial


class home(APIView):
    def get(self,request,format=None):
        data=User_details.objects.all()
        serial=UserSerial(data,many=True)
        return Response(serial.data)

def index(request):
    form=userforms()
    context={'form':form}
    if request.method=="POST":
        invoice_no=request.POST['invoice_no']
        seller_name=request.POST['seller_name']
        seller_address=request.POST['seller_address']
        seller_phone=request.POST['seller_phone']
        buyer_name=request.POST['buyer_name']
        buyer_address=request.POST['buyer_address']
        buyer_phone=request.POST['buyer_phone']

        data={
            'invoice_no':invoice_no,
            'seller_name':seller_name,
            'seller_address':seller_address,
            'seller_phone':seller_phone,
            'buyer_name':buyer_name,
            'buyer_address':buyer_address,
            'buyer_phone':buyer_phone
        }
        data=json.dumps(data)
        header={
            'Content-Type':'application/json'
        }
        r=requests.post("http://127.0.0.1:8000/",data=data,headers=header)
        return HttpResponse("Data Submitted ")
        print(r.json())
        

    return render(request,"home.html",context)
        

