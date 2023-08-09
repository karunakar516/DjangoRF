from django.urls import path,include
from .views import *
from .models import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',CricketerViewSet,basename='cricketer')
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]