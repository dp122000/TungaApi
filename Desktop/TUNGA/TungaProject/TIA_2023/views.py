#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def hello_world(request):

    if request.method == "POST":
         return Response (request.data,status=201)
    
    return Response({"message": "Hello, World!"})