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




def offre(request):
    offres = Offer.objects.all()
    return render(request, 'offre.html', {'offres': offres})


# Offres de la part d'un institut : 
@login_required
def propose_offer(request):
    # Vérifie si l'utilisateur connecté est un établissement
    if hasattr(request.user, 'userprofile') and request.user.userprofile.user_type == 'etablissement':
        if request.method == 'POST':
            form = OfferProForm(request.POST)
            if form.is_valid():
                offer = form.save(commit=False)
                offer.added_by = request.user.userprofile  # Lie l'offre au profil d'établissement
                offer.save()
                messages.success(request, "Offre proposée avec succès.")
                return redirect('offer_success')
        else:
            form = OfferProForm()
        return render(request, 'propose_offer.html', {'form': form})
    else:
        messages.error(request, "Vous n'êtes pas autorisé à proposer une offre.")
        return redirect('home')
