from django import forms
from .models import Student
from .models import Etablissement
from django.contrib.auth.models import User




class student_form(forms.ModelForm):
    # Champs provenant du modèle User
    username = forms.CharField(max_length=150, required=True, label="Prenom.Nom (Nom d'utilisateur)")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email")

    class Meta:
        model = Student
        fields = ['firstname', 'date_of_birth', 'study_domain']  # Champs du modèle Student     plus demandé : 'high_school' 'student_id'
        labels = {
            'firstname': "Prénom",
            'date_of_birth': "Date de naissance",
            'study_domain': "Domaine d'étude",
        }


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
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email")

    class Meta:
        model = Etablissement
        fields = ['adress', 'city', 'country', 'study_domain']  # Champs du modèle Etablissement     plus demandé : 'high_school'
        labels = {
            'adress': "Adresse physique",
            'city': "Ville",
            'country': "Pays",
            'study_domain': "Domaine d'étude",
        }


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
