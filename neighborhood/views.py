from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Profile
from .forms import *
from django.views import generic


@login_required(login_url='/accounts/login/')
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html',{"neighbourhoods":neighbourhoods,})


@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request,'home.html',{"neighbourhoods":neighbourhoods})
