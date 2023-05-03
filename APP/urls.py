from django.contrib import admin
from django.urls import path , include
from APP.views import encriptar ,desencriptamiento
urlpatterns = [
    path('' , encriptar, name="encriptar"),
    path("desencriptamiento/" ,desencriptamiento , name="desencriptamiento")
    # path("desencriptar/" ,desencriptamiento, name="desencriptar"),
]
