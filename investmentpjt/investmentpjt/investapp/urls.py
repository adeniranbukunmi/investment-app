from django.urls import path, re_path
from investmentpjt.investapp import views as investview

urlpatterns =[
    re_path(r'^new_investment/', investview.uploadInvestProduct, name='new_investment'),
    re_path(r'^invest_catalog/', investview.viewCatalog, name='invest_catalog'),
    re_path(r'^edit_investment/(?P<inv_id>\d+)/', investview.editInvestment, name='edit_investment'),
    re_path(r'^delete_investment/(?P<inv_id>\d+)/', investview.deleteInvestment, name='delete_investment'),
    re_path(r'^investment_detail/(?P<inv_id>\d+)/', investview.investmentDetails, name='investment_detail'),
    re_path(r'^buy_investment/(?P<inv_id>\d+)/', investview.buyInvestment, name='buy_investment'),  
    re_path(r'^approve_investment/(?P<inv_id>\d+)/', investview.approveInvestment, name='approve_investment'),  
]

