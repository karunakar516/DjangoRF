from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .models import *
from .serializers import *
class CricketerViewSet(ModelViewSet):
    queryset=Cricketer.objects.all()
    serializer_class=CricketerSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
'''
To make authentication for all classes we include Restframework in settings for clarity see settings restframework  dictionary/json
'''
'''
Similarly for session authentication we change authentication class thats it and we give permission using and changing permission classes
-karunakarbaba
'''