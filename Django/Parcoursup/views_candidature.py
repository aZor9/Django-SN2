from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *
from django.utils import timezone



@login_required
def candidature(request):
    # Vérifie si l'utilisateur est un étudiant
    if request.user.userprofile.user_type != 'student':
        return redirect('home')  # Redirige si ce n'est pas un étudiant

    # Récupère les candidatures de l'étudiant
    applications = Application.objects.filter(student=request.user.userprofile)

    return render(request, 'candidature.html', {'applications': applications})

@login_required
def postuler(request, offer_id):
    # Récupérer l'offre à partir de l'ID
    offre = get_object_or_404(Offer, id=offer_id)

    # Récupérer le profil utilisateur
    user_profile = request.user.userprofile

    # Vérifier si l'utilisateur a déjà postulé pour cette offre
    if Application.objects.filter(student=user_profile, offer=offre).exists():
        messages.warning(request, "Vous avez déjà postulé pour cette offre.")
        return redirect('offre_id', offer_id=offer_id)

    # Si la méthode de requête est POST, créer une nouvelle candidature
    if request.method == "POST":
        # Créer une nouvelle instance d'Application
        application = Application(
            student=user_profile,
            offer=offre,
            application_date=timezone.now(),  # Date actuelle de la candidature
            status='pending'  # Statut par défaut
        )
        application.save()  # Enregistrer l'objet dans la base de données

        # Afficher un message de succès
        messages.success(request, "Votre candidature a été soumise avec succès.")
        return redirect('offre_id', offer_id=offer_id)

    # Si ce n'est pas une méthode POST, redirigez vers l'offre
    return render(request, 'offre.html', {'offre': offre})



@login_required
def gerer_candidature(request, candidature_id):
    # Vérifier si la candidature existe
    try:
        candidature = Application.objects.get(id=candidature_id)
    except Application.DoesNotExist:
        messages.error(request, "La candidature n'existe pas.")
        return redirect('offre_id', offer_id=request.POST.get('offer_id'))  # Rediriger vers l'offre en cas d'erreur
    
    if request.method == 'POST' and request.user.userprofile.user_type == 'etablissement':
        action = request.POST.get('action')
        
        if action == 'accept':
            candidature.status = 'accepted'
            messages.success(request, "La candidature a été acceptée.")
        elif action == 'reject':
            candidature.status = 'rejected'
            messages.warning(request, "La candidature a été refusée.")
        
        candidature.save()

    # Rediriger vers l'offre associée
    return redirect('offre_id', offer_id=candidature.offer.id)
