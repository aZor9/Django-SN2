from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *



def candidature(request):
    candidatures = Application.objects.all()
    return render(request, 'candidature.html', {'candidatures': candidatures})

