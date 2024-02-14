from django.urls import path, re_path
from investmentpjt.investapp import views as investview

urlpatterns =[
    re_path(r'^new_investment/', investview.uploadInvestProduct, name='new_investment'),
    re_path(r'^invest_catalog/', investview.viewCatalog, name='invest_catalog'),
    
]

