from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',StudentCrLi.as_view()),
    path('manipulate/<int:pk>',Studentupdelret.as_view())
]