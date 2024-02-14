from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from .forms import Invest_Product_form 
from .models import Investment_product

# Create your views here.


@login_required

def uploadInvestProduct(request): 
    if request.method == "POST":
        product_form =Invest_Product_form(request.POST or None, request.FILES or None)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.user_id =request.user.id
            product.save()
            messages.success(request, ('Product uploaded successfully!'))
            return HttpResponseRedirect("new_investment")
        else:
            messages.error(request, ('You have error in your form please correct it.'))
            return HttpResponseRedirect("new_investment")
    else:

        Invest_form =  Invest_Product_form()
        return render (request, 'investapp/upload_product_form.html', {'product_form': Invest_form, })
    
@login_required
def viewCatalog(request):
    pass
















