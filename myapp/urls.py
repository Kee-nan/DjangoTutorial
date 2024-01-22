from django.urls import path
from . import views

#This url page are all the various url / places that the program will use
#Each path is a designated url
urlpatterns = [
  path('', views.index, name='index'),
  path('counter', views.counter, name='counter')
]