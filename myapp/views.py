from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from myapp.models import * 
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login
from myapp.models import *
# Create your views here.
def portfolio(request):
    return render(request,'portfolio.html')
def portfolio_detail(request):
    return render(request,'portfolio_detail.html')