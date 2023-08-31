from django.shortcuts import render

from rest_framework.response import Response
# Create your views here.

from rest_framework.decorators import api_view,  permission_classes
@api_view(['GET'])
def home(request):
    

    return Response({"hello":34})
