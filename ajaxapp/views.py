from django.shortcuts import render

from . models import patient

from django.http import JsonResponse

# Create your views here.

def index(request):
    
    
    return render(request,"index.html",)


def getpatient(request):
    
    profiles=patient.objects.all()
    
    return JsonResponse({"profiles":list(profiles.values())})
    
    