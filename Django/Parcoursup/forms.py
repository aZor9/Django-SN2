from django import forms
from .models import OfferPro  # Modifiez le nom ici

class OfferProForm(forms.ModelForm):  # Changez également le nom de la classe
    class Meta:
        model = OfferPro  # Utilisez le modèle OfferPro
        fields = ['title', 'description', 'image_url']  # Listez les champs que vous souhaitez dans le formulaire
