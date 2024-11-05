from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *



def candidature(request):
    candidatures = Application.objects.all()
    return render(request, 'candidature.html', {'candidatures': candidatures})

@login_required
def postuler(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    student_profile = request.user.userprofile

    # Vérifie si l'utilisateur est un étudiant et n'a pas déjà postulé
    if student_profile.user_type == 'student':
        if not Application.objects.filter(student=student_profile, offer=offer).exists():
            Application.objects.create(student=student_profile, offer=offer, status='pending')
            messages.success(request, 'Votre candidature a été soumise avec succès.')
        else:
            messages.info(request, 'Vous avez déjà postulé pour cette offre.')
    else:
        messages.error(request, "Seuls les étudiants peuvent postuler à cette offre.")

    return redirect('offre_id', offer_id=offer.id)