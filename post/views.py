from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def post(requset):
    return HttpResponse('day la bai viet')


def post2(request):
    return HttpResponse('day la bai viet  2')
