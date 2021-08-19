from django.db import models
from django.db.models.base import Model, ModelState

class User_details(models.Model):
    invoice_no=models.CharField(max_length=20)
    invoice_date=models.DateTimeField(auto_now_add=True)
    seller_name=models.CharField(max_length=30)
    seller_address=models.CharField(max_length=30)
    seller_phone=models.CharField(max_length=20)
    buyer_name=models.CharField(max_length=20)
    buyer_address=models.CharField(max_length=40)
    buyer_phone=models.CharField(max_length=30)


class Products(models.Model):
    name=models.CharField(max_length=20)
    quantity=models.IntegerField()
    amount=models.IntegerField(default=0)
    user=models.ForeignKey(User_details,on_delete=models.PROTECT,related_name='products')
    
    def __str__(self):
        return self.name,self.quantity