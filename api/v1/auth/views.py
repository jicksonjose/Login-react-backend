from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from loginapp.models import UserModel
import json
from .serializer import *
from django.db.models import Q

@csrf_exempt
def loginApi(request):
    if request.method == 'POST':
        receieved_data = json.loads(request.body)
        print(receieved_data)
        getemail = receieved_data["email"]
        getpassword = receieved_data["password"]
        data = list(UserModel.objects.filter(Q(email__exact=getemail) & Q(password__exact=getpassword)).values())
        return HttpResponse(json.dumps(data)) 
    else:
        return HttpResponse(json.dumps({"status": "login details Invalid"})) 