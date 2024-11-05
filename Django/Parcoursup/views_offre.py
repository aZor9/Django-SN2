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
    # Récupérer les critères de recherche depuis les paramètres GET
    query = request.GET.get('query', '')
    selected_category = request.GET.get('category', '')

    # Filtrer les offres en fonction des critères
    offres = Offer.objects.all()
    if query:
        offres = offres.filter(title__icontains=query)  # Filtrer par nom de l'offre (partiellement)
    if selected_category:
        offres = offres.filter(study_domain=selected_category)  # Filtrer par domaine d'étude

    study_domains = UserProfile.STUDY_DOMAINS  # Liste des domaines pour le menu déroulant

    context = {
        'offres': offres,
        'study_domains': study_domains,
        'query': query,
        'selected_category': selected_category,
    }
    return render(request, 'offre.html', context)

def offre(request, offer_id):
    # Récupérer l'offre
    offre = get_object_or_404(Offer, id=offer_id)

    # Récupérer toutes les candidatures associées à l'offre spécifiée
    candidatures = Application.objects.filter(offer_id=offer_id)

    # Vérifier si l'utilisateur connecté a déjà postulé
    user = request.user
    has_applied = Application.objects.filter(student__user=user, offer=offre).exists()

    # Passer les candidatures et l'information de candidature au template
    context = {
        'candidatures': candidatures,
        'offre': offre,
        'has_applied': has_applied,
    }
    return render(request, 'offre_detail.html', context)

# def offre_create(request):
#     return render(request, 'offre_create.html')

# def offer_success(request):
#     return render(request, 'offre.html')

def offre_create(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.added_by = request.user.userprofile  # Assurez-vous que l'utilisateur a un profil
            offer.save()
            # return redirect('offer_success')  # Rediriger vers une page de succès
    else:
        form = OfferForm()
    
    return render(request, 'offre_create.html', {'form': form})
