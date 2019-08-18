from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({"code": -1, "info": "user is not existed"})