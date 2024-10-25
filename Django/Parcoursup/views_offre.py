from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *



def offres(request):
    offres = Offer.objects.all()
    return render(request, 'offre.html', {'offres': offres})

def offre(request):
    offres = Offer.objects.all()
    return render(request, 'offre.html', {'offres': offres})