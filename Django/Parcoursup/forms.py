from django import forms
from .models import OfferPro  # Modifiez le nom ici
from models import Student

class OfferProForm(forms.ModelForm):  # Changez également le nom de la classe
    class Meta:
        model = OfferPro  # Utilisez le modèle OfferPro
        fields = ['title', 'description', 'image_url']  # Listez les champs que vous souhaitez dans le formulaire

class student_form(forms.ModelForm):
    class Meta :
        model = Student
        fields = ('name', 'firstname', 'email')