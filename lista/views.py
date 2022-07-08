from django.shortcuts import render
from urllib import request

# Create your views here.
def Inicio(request):
    return render(request, 'lista/index.html')
