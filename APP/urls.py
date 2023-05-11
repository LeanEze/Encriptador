from django.contrib import admin
from django.urls import path , include
from APP.views import encriptar



urlpatterns = [
    
    path('' , encriptar, name="encriptar"),

]
