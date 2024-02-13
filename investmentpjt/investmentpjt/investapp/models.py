from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Investment_product(models.Model):

    catalog_field = [
        ("Agriculture", "Agriculture"),
        ("Electronicą", "Electronics"),
        ("Real Estate", "Real Estate"),
        ("Forex", "Forex"),
        ("Cryptocurrency", "Cryptocurrency"),
        ("Solar energy", "Solar energy"),
    ]



    invest_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    investment_name = models.CharField(unique=True, max_length=50)
    date_upload= models.DateTimeField(auto_now_add =True, unique=True)
    total_unit= models.IntegerField(unique=False, null=False)
    minimum_unit= models.IntegerField(unique=False, null=False)
    maximum_unit= models.IntegerField(unique=False, null=False)
    price_per_unit= models.IntegerField(unique=False, null=False)
    description= models.CharField(unique=False, max_length=500,  null=False)
    product_picture = models.ImageField(upload_to='productImage/', unique=False, null=True)
    category = models.CharField(choices=catalog_field, max_length=20, default=None)
    approved = models.CharField(unique=False, max_length=10, null=True, default= "unapproved")
    category_display = models.BooleanField(default=False, unique=False)

