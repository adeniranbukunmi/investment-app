from django.db import models
from investmentpjt.investapp.models import Investment_product
from django.contrib.auth.models import User

# Create your models here.
class Wallet_Account_table(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    wallet_balance = models.IntegerField(null = False, unique =False)
    wallet_address= models.CharField(unique =False, max_length=10)
    

class Wallet_Transaction_table(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    wallet= models.ForeignKey(Wallet_Account_table, on_delete = models.CASCADE)
    transaction_type= models.CharField(unique =False, max_length=20)
    transaction_date = models.DateTimeField(auto_now_add=True, unique=False)
    wallet_address= models.CharField(unique =False, max_length=10)
    transaction_amount = models.BigIntegerField(unique =False, null = True)


class Investment_order_table(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    investment= models.ForeignKey(Investment_product, on_delete = models.CASCADE)
    unit_price = models.IntegerField(null = False, unique =False)
    total_price = models.IntegerField(null = False, unique =False)
    date_created = models.DateTimeField(auto_now_add= True, unique=False)
    unit_ordered = models.IntegerField(null = False, unique =False)
    due_date = models.DateField(null = False, unique =False)
    amount_paid = models.IntegerField(null = False, unique =False)

class Investment_Update_table(models.Model):
    update_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    investment= models.ForeignKey(Investment_product, on_delete = models.CASCADE)
    interest= models.IntegerField(null = False, unique =False)
    investment_balance = models.IntegerField(null = False, unique =False)
    date_created = models.DateTimeField(auto_now_add= True, unique=False)