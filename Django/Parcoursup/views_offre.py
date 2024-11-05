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


def offre(request, offer_id):
    offre = get_object_or_404(Offer, id=offer_id)
    return render(request, 'offre_detail.html', {'offre': offre})

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
