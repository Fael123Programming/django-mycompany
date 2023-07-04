from django.shortcuts import render
from django.http import HttpResponse

# class MainView():
#     pass

def MainView(request, *args, **kwargs):
    return HttpResponse('<h1 style="text-align: center;">CUSTOMERS</h1>')    
