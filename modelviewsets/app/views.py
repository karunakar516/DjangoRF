from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
class CricketerViewSet(ModelViewSet):
    queryset=Cricketer.objects.all()
    serializer_class=CricketerSerializer