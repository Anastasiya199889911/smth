from django.shortcuts import render
import requests
import bs4
from . import models
import random
from django.http import HttpResponse, JsonResponse
import json
import lxml.html

# Create your views here.


def Profile(request):
    id=request.session.get('userid','no')
    if(id!='no'):
        id = request.session['userid']
        name = request.session['username']
        email = request.session['useremail']
        return render(request, 'Profile/Profile.html', locals())
    else:
        return render(request, 'Main/Authorization.html', locals())


