from django.shortcuts import render
from django.http import HttpResponse


def hello_guys(request):
    return render(request,'index.html',{ 'name': 'sia raji' })


# Create your views here.
