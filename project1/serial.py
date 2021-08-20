from rest_framework import serializers
from rest_framework.views import set_rollback
from .models import Products,User_details

class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('name','quantity','amount')


class UserSerial(serializers.ModelSerializer):
    products=ProductSerial(many=True)

    def create(self,validated_data):
        products_data=validated_data.pop('products')
        users=User_details.objects.create(**validated_data)
        for data in products_data:
            Products.objects.create(user=users,products=data)
        return users
    class Meta:
        model=User_details
        fields=('invoice_no','invoice_date','seller_name','seller_address','seller_phone','buyer_name','buyer_address','buyer_phone','products')

    
