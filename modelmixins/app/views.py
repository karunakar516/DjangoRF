from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
)
#Instead of using ListModel,CreateModel in one class You can Use two different classes
class StudentCrLi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
#Instead of using UpdateMixin,DestroyMixin,RetrieveMixin in one class You can Use two different classes
class Studentupdelret(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)

