from django.contrib import admin
from django.urls import path , include
from APP.views import miEncriptador
urlpatterns = [
    path('' , miEncriptador, name="Encriptador")
]
