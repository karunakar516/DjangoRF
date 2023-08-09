from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('add',addst),
    path('update/<int:id>',updatest),
    path('delete/<int:id>',delst)
]