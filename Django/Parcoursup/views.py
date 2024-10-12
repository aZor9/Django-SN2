# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World et Bonjour")




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Program

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
