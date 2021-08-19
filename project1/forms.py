from django import forms
from django import forms
from .models import User_details,Products

class userforms(forms.ModelForm):
    class Meta:
        model=User_details
        fields="__all__"


class product_forms(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"