from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def post(request):
    return render(request, 'post/post.html')
