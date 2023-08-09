from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
#read
@api_view(['GET'])
def home(request):
    studob=Student.objects.all()
    serializer=StudentSerializer(studob,many=True)
    return Response(serializer.data)
#create
@api_view(['POST'])
def addst(request):
    studob=Student.objects.all()
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#update
@api_view(['POST'])
def updatest(request,id):
    studob=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=studob,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#delete
@api_view(['DELETE'])
def delst(request,id):
    studob=Student.objects.get(id=id)
    studob.delete()
    return Response("item deleted")