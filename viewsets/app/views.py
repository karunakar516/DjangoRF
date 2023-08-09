from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
class CricketerViewSet(ViewSet):
    def list(self,request):
        queryset=Cricketer.objects.all()
        serializer=CricketerSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk):
        id=pk
        if id is not None:
            queryset=Cricketer.objects.get(id=id)
            serializer=CricketerSerializer(queryset)
            return Response(serializer.data)
        return Response("enter correct id")
    def update(self,request,pk):
        id=pk
        if id is not None:
            queryset=Cricketer.objects.get(id=id)
            serializer=CricketerSerializer(queryset,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data updated")
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response("enter correct id")
    def destroy(self,request,pk):
        id=pk
        queryset=Cricketer.objects.get(id=id)
        queryset.delete()
        return Response("data deleted")
    def create(self,request):
        serializer=CricketerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)