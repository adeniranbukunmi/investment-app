from django.contrib import admin
from django.urls import path, include, re_path
from investmentpjt.userapp import views as vw


urlpatterns =[
    re_path(r'^my_profile/(?P<u_id>\d+)/', vw.myProfile, name='my_profile'),
    re_path(r'^edit_profile/(?P<u_id>\d+)/', vw.editProfile, name='edit_profile'),
    re_path(r'^deactivate_profile/(?P<u_id>\d+)/', vw.deactivateProfile, name='deactivate_profile'),
    re_path(r'^display_users/(?P<value>\w+)/', vw.displayUsers, name='display_users'),
    re_path(r'^delete_profile/(?P<u_id>\d+)/', vw.deleteProfile, name='delete_profile'),
]
