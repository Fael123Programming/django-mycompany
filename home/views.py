from django.shortcuts import render
from django.http import HttpResponse

def Index(request, *args, **kwargs):
    return render(request, 'home/index.html')
