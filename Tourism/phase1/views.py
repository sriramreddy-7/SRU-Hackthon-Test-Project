from urllib import request
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def plan_trip(request):
    return render(request,'plan_trip.html')

def medaram_jatra(request):
    return render(request,'medaram_jatra.html')

def rampaa(request):
    return render(request,'rampaa.html')

def Warangal_Fort(request):
    return render(request,'Warangal_Fort.html')