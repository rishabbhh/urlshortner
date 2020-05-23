

# Create your views here.

from django.shortcuts import render,redirect
import pyshorteners

def index(request):
    return render(request,'home.html')


def shorti(request):
    link = request.GET['urltowork']
    shortener = pyshorteners.Shortener()
    res = shortener.tinyurl.short(link)
    
    context={
             "shortened":res,
             

        }

    
    return render(request,'home.html',context)
