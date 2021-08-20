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

class home(APIView):
    def get(self,request,format=None):
        userform=userforms()
        productform=product_forms()
        context={'uform':userform,'pform':productform}
        return render(request,"home.html",context)
    def post(self,request,format=None):
        userform=userforms(request.POST or None)
        invoice_no=userform.cleaned_data.get('invoice_no')
        seller_name=userform.cleaned_data['seller_name']
        seller_address=userform.cleaned_data['seller_address']
        seller_phone=userform.cleaned_data['seller_phone']
        buyer_name=userform.cleaned_data['buyer_name']
        buyer_address=userform.cleaned_data['buyer_address']
        buyer_phone=userform.cleaned_data['buyer_phone']
        product_form=product_forms(request.POST or None)
        name=product_form.cleaned_data['name']
        qunatity=product_form.cleaned_data['quantity']
        amount=product_form.cleaned_data['amount']
        user=product_form.cleaned_data['user']
        
        data1={
        'invoice_no':invoice_no,
        'seller_name':seller_name,
        'seller_address':seller_address,
        'seller_phone':seller_phone,
        'buyer_name':buyer_name,
        'buyer_address':buyer_address,
        'buyer_phone':buyer_phone
                }
        data2={
            'name':name,
            'quantity':qunatity,
            'amount':amount,
            'user':user
        }
        serial1=UserSerial(data=data1)
        serial2=ProductSerial(data=data2)
        if serial1.is_valid() and serial2.is_valid():
            serial1.save()
            serial2.save()
            
            return Response(serial1.data)