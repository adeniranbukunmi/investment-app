from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class Profile(models.Model):
    countries = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United Kingdom", "UK"),
        ("USA", "USA"),
    ]

    states = [
        ("Abia", "Abia"),
        ("Oyo", "Oyo"),
        ("Osun", "Osun"),
        ("Lagos", "Lagos"),
        ("Kano", "Kano"),
        ("Abuja", "Abuja"),

    ]
    position= [
        ("MD", "MD"),
        ("CEO", "CEO"),
        ("HOD", "HOD"),
        ("Accountant", "Accountant"),
        ("Secretary", "Secretary"),
        ("Admin", "Admin"),
        ("Store keeper", "Store keeper"),
        ("product Manager", "product Manager"),
        ("Delivery Agent", "Delivery Agent"),

    ]

    dept= [
        ("Customer care", "Customer care"),
        ("Sales", "Sales"),
        ("Account", "Account"),
        ("HR", "HR"),
        ("Marketing", "Marketing"),
    ]
    Ma_status= [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicated", "Complicated"),
    ]

    staff_status= [
        ("Active", "Active"),
        ("Suspended", "Suspended"),
        ("On leave", "On leave"),
        ("Resigned", "Resigned"),
        ("Retired", "Retired"),

    ]
    identity_name= [
        ("International Passport", "International Passport"),
        ("Driver's license", "Driver's license"),
        ("Voter's card", "Voter's card"),
        ("Resigned", "Resigned"),
        ("NIMC", "NIMC"),

    ]

    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(unique=False, max_length=150, null=True)
    phone= models.CharField(unique=True, max_length=11, null=True)
    date_of_birth = models.DateField(unique=False, max_length=11, null=True)
    gender= models.CharField(unique=False, max_length=6, null=True)
    nationality= models.CharField(choices=countries, unique=False, max_length=50, null=True)
    state= models.CharField( choices=states, unique=False, max_length=20, null=True)
    identity_card_name = models.CharField(choices=identity_name, unique=False, max_length=150, null=True)
    identity_card_number = models.CharField( unique=True, max_length=15, null=True)
    means_of_identity = models.ImageField(upload_to='identityImage/', unique=False, null=True)
    profile_picture = models.ImageField(upload_to='profileImage/', unique=False, null=True)
    position = models.CharField(choices=position, unique=False, max_length=25, null=True)
    department = models.CharField(choices=dept, unique=False, max_length=25, null=True)
    marital_status = models.CharField(choices=Ma_status, unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False)
    next_of_kin= models.CharField(unique=False, max_length=20, null=True)
    status = models.CharField(choices=staff_status, unique=False, max_length=10, null=True, default='Active')


# now this where the magic happens: we will now define signals so our Profile model will be automatically created upon/updated when we create/updated user instances question: is this a must, is there other way of doing this below, if yes example:

    @receiver(post_save, sender =User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()