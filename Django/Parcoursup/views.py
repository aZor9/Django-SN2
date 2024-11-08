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
            return redirect('login')
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
            return redirect('login')
    else:
        form = EtablissementForm()

    return render(request, 'register_etablissement.html', {'form': form})


def edit_student_profile(request):
    # Vérifie que l'utilisateur est un étudiant
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.user_type != 'student':
        return redirect('home')  # Redirige si l'utilisateur n'est pas un étudiant

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            # Ajoutez un message de succès
            success_message = "Profil mis à jour avec succès !"
            return render(request, 'profile_student.html', {'form': form, 'success_message': success_message})
        else:
            # Ajoutez un message d'erreur
            error_message = "Une erreur est survenue. Veuillez réessayer."
            return render(request, 'profile_student.html', {'form': form, 'error_message': error_message})
    else:
        form = StudentProfileForm(instance=user_profile)

    return render(request, 'profile_student.html', {'form': form})