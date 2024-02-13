from django import forms
from .models import Investment_product


class Invest_Product_form(forms.ModelForm):
    
    class Meta:
        model = Investment_product
        exclude =(
            'invest_id',
            'user',
            'date_upload'
        )
        widgets ={
            'description':forms.Textarea(attrs={'cols':100, 'row':10})
        }

