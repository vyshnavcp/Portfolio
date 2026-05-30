from myapp.models import Banner
from myapp.models import Portfolio
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
    portfolio=Portfolio.objects.all()
    banner=Banner.objects.all()
    return render(request,'portfolio.html',{'portfolio':portfolio,'banner':banner})
def portfolio_detail(request,slug):
    portfolio=Portfolio.objects.get(slug=slug)
    prev_project = Portfolio.objects.filter(id__lt=portfolio.id).order_by('-id').first()
    next_project = Portfolio.objects.filter(id__gt=portfolio.id).order_by('id').first()
    return render(request,'portfolio_detail.html',{'portfolio':portfolio,'prev_project': prev_project,'next_project': next_project})
