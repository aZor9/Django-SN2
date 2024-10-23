from django import forms
from .models import OfferPro  
from .models import Student
from .models import Etablissement
from django.contrib.auth.models import User


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
        fields = ['firstname', 'date_of_birth', 'study_domain', 'student_id']  # Champs du modèle Student     plus demandé : 'high_school'

    def save(self, commit=True):
        # Sauvegarde des informations User et Student
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        
        student = super(student_form, self).save(commit=False)
        student.user = user  # Associe l'utilisateur créé avec l'étudiant
        
        if commit:
            user.save()
            student.save()
        return student







class Etablissement_form(forms.ModelForm):
    # Champs provenant du modèle User
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Etablissement
        fields = ['username', 'adress', 'city', 'country']  # Champs du modèle Etablissement     plus demandé : 'high_school'

    def save(self, commit=True):
        # Sauvegarde des informations User et Etablissement
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        

        Etablissement = super(Etablissement_form, self).save(commit=False)
        Etablissement.user = user  
        
        if commit:
            user.save()
            Etablissement.save()
        return Etablissement
