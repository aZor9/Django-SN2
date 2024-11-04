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
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'register_student.html', {'form': form})

## Incription Etablissement
def register_etablissement(request):
    if request.method == 'POST':
        form = EtablissementForm(request.POST)
        
        if form.is_valid():
            form.save()
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
    if request.user.is_authenticated and request.user.is_etablissement:  # Vérifie si l'utilisateur est une etablissement
        if request.method == 'POST':
            form = OfferProForm(request.POST)  # Utilisez le formulaire OfferPro
            if form.is_valid():
                offer = form.save(commit=False)
                offer.etablissement = request.user.etablissement  # Assurez-vous d'avoir une relation entre l'utilisateur et l'etablissement
                offer.save()
                return redirect('offer_success')  # redirige vers une page de succès ou une autre page après soumission
        else:
            form = OfferProForm()  # Utilisez le formulaire OfferPro
        return render(request, 'propose_offer.html', {'form': form})
    else:
        return redirect('home')  # Redirige vers la page d'accueil si l'utilisateur n'est pas autorisé