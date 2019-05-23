from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def submit_account(request):
    '''user submits an account information'''
    print("i am in submit account")
    print(request.POST)

    return JsonResponse({ 'status': 'ok', }, encoder=JSONEncoder)
