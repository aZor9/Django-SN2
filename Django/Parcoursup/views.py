from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Program, Offer

from .models import OfferPro  # Modifiez le nom ici
from .forms import OfferProForm  # Modifiez le nom ici

def hello_world(request):
    return HttpResponse("Hello, World et Bonjour")


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


def index (request):
   return render(request, 'index.html')


def home (request):
    programs = Program.objects.filter(etablissement__is_validated=True)  # On affiche seulement les offres validées
    return render(request, 'home.html', {'programs': programs})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a été créé avec succès, {username} !')
            return redirect('login')  # Redirection vers la page de connexion après inscription
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



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