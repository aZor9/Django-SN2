from django import forms
from django.contrib.auth.models import User
from .models import Student, Etablissement, UserProfile

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email")

    class Meta:
        model = Student
        fields = ['firstname', 'date_of_birth', 'study_domain']
        labels = {
            'firstname': "Prénom",
            'date_of_birth': "Date de naissance",
            'study_domain': "Domaine d'étude",
        }

    def clean(self):
        cleaned_data = super().clean()
        # Validation des champs requis
        if not cleaned_data.get("firstname"):
            self.add_error('firstname', "Ce champ est requis.")
        if not cleaned_data.get("date_of_birth"):
            self.add_error('date_of_birth', "Ce champ est requis.")
        if not cleaned_data.get("study_domain"):
            self.add_error('study_domain', "Ce champ est requis.")
        return cleaned_data

    def save(self, commit=True):
        # Création de l'utilisateur associé
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        # Création du UserProfile pour l'étudiant
        if commit:
            UserProfile.objects.create(user=user, user_type='student')

        # Création de l'objet Student
        student = super().save(commit=False)
        student.user = user
        student.email = self.cleaned_data['email']  # Associe l'email à l'objet Student

        if commit:
            student.save()
        return student


class EtablissementForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email")

    class Meta:
        model = Etablissement
        fields = ['name', 'adress', 'city', 'country', 'study_domain']
        labels = {
            'name': "Nom de l'établissement",
            'adress': "Adresse",
            'city': "Ville",
            'country': "Pays",
            'study_domain': "Domaine d'étude",
        }

    def clean(self):
        cleaned_data = super().clean()
        # Validation des champs requis
        if not cleaned_data.get("name"):
            self.add_error('name', "Ce champ est requis.")
        if not cleaned_data.get("adress"):
            self.add_error('adress', "Ce champ est requis.")
        if not cleaned_data.get("city"):
            self.add_error('city', "Ce champ est requis.")
        if not cleaned_data.get("country"):
            self.add_error('country', "Ce champ est requis.")
        if not cleaned_data.get("study_domain"):
            self.add_error('study_domain', "Ce champ est requis.")
        return cleaned_data

    def save(self, commit=True):
        # Création de l'utilisateur associé
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        # Création du UserProfile pour l'établissement
        if commit:
            UserProfile.objects.create(user=user, user_type='etablissement')

        # Création de l'objet Etablissement
        etablissement = super().save(commit=False)
        etablissement.user = user

        if commit:
            etablissement.save()
        return etablissement
