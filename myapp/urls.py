from os import name
from myapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
path('',views.portfolio,name='portfolio'),
path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),]
