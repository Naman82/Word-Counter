from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return render(request,'index.html')

def counter(request):
    text=request.GET['text']
    words=len(text.split())
    return render(request,'counter.html',{'word':words})


