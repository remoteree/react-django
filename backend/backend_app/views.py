from django.shortcuts import render
from django.http import JsonResponse
import datetime

# Create your views here.
def test(request):
    return JsonResponse( {'message': f"Server is running as of {str(datetime.datetime.now())}"}, status=200)
