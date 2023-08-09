from django.urls import path
from .views import *
urlpatterns = [
    path('',InternLiCre.as_view()),
    path('manipulate/<int:pk>',Internupdelret.as_view())
]