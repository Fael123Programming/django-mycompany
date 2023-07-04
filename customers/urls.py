from django.urls import path
from . import views

appname='customers'
urlpatterns = [
    path('', views.MainView, name='MainView')    
]
