from rest_framework import serializers
from rest_framework.views import set_rollback
from .models import Products,User_details

class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('id','name','quantity','amount','user')


class UserSerial(serializers.ModelSerializer):
    products=ProductSerial(many=True,read_only=True)
    class Meta:
        model=User_details
        fields=('id','invoice_no','invoice_date','seller_name','seller_address','seller_phone','buyer_name','buyer_address','buyer_phone','products')
