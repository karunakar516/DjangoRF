from django.shortcuts import render
from rest_framework.generics import (ListAPIView,CreateAPIView,ListCreateAPIView,
                                     UpdateAPIView,RetrieveAPIView,DestroyAPIView,
                                     RetrieveDestroyAPIView,RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from .models import *
from .serializers import *
class InternLiCre(ListCreateAPIView):
    queryset=Intern.objects.all()
    serializer_class=InternSerializer
class Internupdelret(RetrieveUpdateDestroyAPIView):
    queryset=Intern.objects.all()
    serializer_class=InternSerializer
'''
These are derived/inherited from combining generic api view with mixins we can use individually if we want     -karunakarbaba
'''