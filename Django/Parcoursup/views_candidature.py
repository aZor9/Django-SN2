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



def candidature(request):
    candidatures = Application.objects.all()
    return render(request, 'candidature.html', {'candidatures': candidatures})

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