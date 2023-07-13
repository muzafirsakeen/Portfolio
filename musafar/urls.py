from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homes, name='home'),
    # path('detection/', views.emotion_detection, name='emotion-detection'),
    path('contact',views.contact,name='contact')


   

    


]