from django.urls import path
from . import views

#urlConf
urlpatterns =[
    path('hello/',views.hello_guys)
]