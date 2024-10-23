from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


## Admin : 
# Vérifie si l'utilisateur est admin
def is_admin(user):
    return user.is_superuser

# Vue principale d'administration
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Sous-page pour la gestion des utilisateurs
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()  # Récupère tous les utilisateurs
    return render(request, 'manage_users.html', {'users': users})

# Modifier le rôle de l'utilisateur
@user_passes_test(is_admin)
def change_user_role(request, user_id, role):
    user = get_object_or_404(User, id=user_id)
    if role == 'student':
        user.is_staff = False
        user.is_superuser = False
    elif role == 'etablissement':
        user.is_staff = True  # Par exemple, pour les etablissements
    elif role == 'admin':
        user.is_superuser = True  # Admin
    user.save()
    messages.success(request, f"Le rôle de {user.username} a été changé en {role}.")
    return redirect('manage_users')

# Sous-page pour la gestion des offres
@user_passes_test(is_admin)
def manage_offers(request):
    offers = Offer.objects.all()
    return render(request, 'manage_offers.html', {'offers': offers})

# Accepter ou refuser une offre
@user_passes_test(is_admin)
def approve_offer(request, offer_id, action):
    offer = get_object_or_404(Offer, id=offer_id)
    if action == 'approve':
        offer.is_approved = True
    elif action == 'reject':
        offer.is_approved = False
    offer.save()
    messages.success(request, f"L'offre {offer.title} a été {action}ée.")
    return redirect('manage_offers')

