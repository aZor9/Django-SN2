from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Déconnexion réussie !") 
            return redirect('home')  
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def home (request):
    return render(request, 'home.html')

## Incription Etudiant
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        
        if form.is_valid():
            user_profile = form.save()  # Création de UserProfile via le formulaire
            login(request, user_profile.user)  # Connexion automatique de l'utilisateur après inscription
            messages.success(request, "Inscription réussie ! Bienvenue, étudiant.")
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'register_student.html', {'form': form})



## Incription Etablissement
def register_etablissement(request):
    if request.method == 'POST':
        form = EtablissementForm(request.POST)
        
        if form.is_valid():
            user_profile = form.save()  # Création de UserProfile via le formulaire
            login(request, user_profile.user)  # Connexion automatique de l'utilisateur après inscription
            messages.success(request, "Inscription réussie ! Bienvenue, établissement.")
            return redirect('home')
    else:
        form = EtablissementForm()

    return render(request, 'register_etablissement.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')