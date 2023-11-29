from django.shortcuts import render
from django.template import RequestContext
from django.template.context import Context
from django.http import JsonResponse
from .models import *
#from django.db.models import Q

# Create your views here.

def accueil(request):
    return render(request,'app/index.html')
    
