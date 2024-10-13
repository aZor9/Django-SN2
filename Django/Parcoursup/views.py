from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Program



def hello_world(request):
    return HttpResponse("Hello, World et Bonjour")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('home')  # Remplacez 'home' par le nom de votre page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def index (request):
   return render(request, 'index.html')


def home (request):
    programs = Program.objects.filter(institution__is_validated=True)  # On affiche seulement les offres validées
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