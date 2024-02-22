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
    invest = Investment_product.objects.all()
    return render(request=request, template_name='investapp/investment_view.html', context={'invest':invest})




def approveInvestment (request, inv_id):
    product = Investment_product.objects.get(invest_id=inv_id)
    if product.approved == "Unapproved":
        Investment_product.objects.filter(invest_id=inv_id).update(approved="Approved")
    else:
        Investment_product.objects.filter(invest_id=inv_id).update(approved="Unapproved")
    return viewCatalog(request=request)

@login_required
def investmentDetails(request, inv_id):
    product = Investment_product.objects.filter(invest_id=inv_id)
    return render(request=request, template_name='investapp/investment_details.html', context={'investment':product})


login_required
def editInvestment(request, inv_id):
    product = get_object_or_404(Investment_product, invest_id=inv_id)
    if request.method == 'POST':
        edit_invest_form = Invest_Product_form(request. POST or None, request.FILES or None, instance=product)
        if edit_invest_form.is_valid():
            edit_invest_form.save()
            messages.success(request, ('Product was successfully updated!'))
            return viewCatalog(request=request)
        else:
            messages.error(request, ('Form not correctly filled.'))
            return HttpResponsePermanentRedirect(reverse('edit_investment', args=(inv_id)))

    
    else:
        product_form = Invest_Product_form(instance=product)
        return render(request,'investapp/upload_product_form.html',{"product_form":product_form,})
    
@login_required
def deleteInvestment(request, inv_id):
    Investment_product.objects.filter(invest_id=inv_id).delete()
    messages.success(request, ('Product was successfully deleted!'))
    return viewCatalog(request=request)



def marketPlace(request):
    invest = Investment_product.objects.filter(approved ="Approved")
    return render(request, "index.html", {'investment':invest})

@login_required
def buyInvestment(request, inv_id):
    pass


# @login_required
# def approveInvestment (request, inv_id):
#     product = Investment_product.objects.filter(invest_id=inv_id)
#     if product.values()[0].get("approved") == "Unapproved":
#         Investment_product.objects.filter(invest_id=inv_id).update(approved="Approved")
#     else:
#         Investment_product.objects.filter(invest_id=inv_id).update(approved="Unapproved") this is an alternative method of doing the function above























