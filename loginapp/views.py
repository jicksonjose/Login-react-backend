from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from loginapp.models import UserModel
import json
from loginapp.serializer import *
from django.db.models import Q
# Create your views here.


