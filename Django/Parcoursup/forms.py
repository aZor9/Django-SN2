from django import forms
from .models import OfferPro  
from .models import Student


class OfferProForm(forms.ModelForm):  # Changez également le nom de la classe
    class Meta:
        model = OfferPro  # Utilisez le modèle OfferPro
        fields = ['title', 'description', 'image_url']  # Listez les champs que vous souhaitez dans le formulaire

class student_form(forms.ModelForm):
    # Champs provenant du modèle User
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Student
        fields = ['firstname', 'date_of_birth', 'high_school', 'study_domain', 'student_id']  # Champs du modèle Student



