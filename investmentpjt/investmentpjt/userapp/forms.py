from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(max_length=30, required=False, help_text="optional")
    last_name= forms.CharField(max_length=30, required=False, help_text="optional")
    email = forms.EmailField(max_length=100,  help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        
class User_form(forms.ModelForm):
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email')
# this is where signup form ends

# edit profile starts
class Edit_Profile_form(forms.ModelForm):
    gend = [
        ("male", "male"),
        ("Female", "Female"),
        ]
    position =[
        ("HD", "HD"),
        ("CEO", "CEO"),
        ("HOD", "HOD"),
        ("Accountant", "Accountant"),
        ("Secretary", "Secretary"),
        ("Admin", "Admin"),
        ("Customer care", "Customer care"),
        ]
    dept = [
        ("Customer care", "Customer care"),
        ("Account", "Account"),
        ("HR", "HR"),
        ("Marketing", "Marketing"),
        ]

    staff_status=[
        ("Active", "Active"),
        ("Suspended", "Suspended"),
        ("On leave", "On leave"),
        ("Resigned", "Resigned"),
        ("Retired", "Retired"),
        ]
# the above are fields having dropdown

    profile_picture = forms.ImageField(required=False, label='profile picture')    
    means_of_identity = forms.ImageField(required=False, label = 'Means of identity') 
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    position = forms.ChoiceField(choices=position, required=False)
    department = forms.ChoiceField(choices=dept, required=False)
    status = forms.ChoiceField(choices=staff_status, required=False)

# this is how to over ride a compulsory field by setting it to false


    class Meta:
        model = Profile
        fields =[
            'address',
            'phone',
            'date_of_birth',
            'gender',
            'nationality',
            'state',
            'identity_card_name',
            'identity_card_number',
            'means_of_identity',
            'profile_picture',
            'position', 
            'department',
            'marital_status',
            'next_of_kin',
            'status', 
            'staff',
            ]
#the above is the fields that the user will fill  

        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type': 'date'}),
                }
        # 
    
    # class Meta:
    #         model = profile
    #         exclude = [
    #         "profile_id",
    #         "user",
    #         ]
    # you can use this to exclude few fields from what the user will fill but if any is compulsory, over ride it by setting it to false








































