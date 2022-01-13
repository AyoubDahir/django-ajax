from django.shortcuts import render

from . models import patient

from django.http import JsonResponse

# Create your views here.

def index(request):
    patients=patient.objects.all()
    
    
    return render(request,"index.html",{"patients":patients})


def getpatient(request):
    
    profiles=patient.objects.all()
    
    return JsonResponse({"profiles":list(profiles.values())})
    
    