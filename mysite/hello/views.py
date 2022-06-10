from django.shortcuts import render
from requests import request
from django.http import HttpResponse
from urllib3 import HTTPResponse

# Create your views here.
def myview(request):
    return HttpResponse('hello from hello app')