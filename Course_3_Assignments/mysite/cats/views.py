from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def testview(req):
    return HttpResponse("hello from cats app")
