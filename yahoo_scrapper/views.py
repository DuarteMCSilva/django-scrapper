from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework.response import Response
#from rest_framework.decorators import api_view


# Create your views here.
#@api_view(['GET'])
#def getData(request):
#return Response()

def getData(request):
    return HttpResponse('YAHOOO!')

def hello(request):
    return HttpResponse('Hello!')