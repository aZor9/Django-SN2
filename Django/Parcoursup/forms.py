from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Offer

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email")
    firstname = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['firstname', 'study_domain']
        labels = {
            'firstname': "Prénom",
            'study_domain': "Domaine d'étude",
            # 'date_of_birth': "Date de naissance",
        }

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        user_profile = super().save(commit=False)
        user_profile.user = user
        user_profile.user_type = 'student'
        
        if commit:
            user_profile.save()
        return user_profile


class EtablissementForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email")
    name = forms.CharField(required=True)
    adress = forms.CharField(required=True)
    city = forms.CharField(required=True)
    country = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'adress', 'city', 'country', 'study_domain']
        labels = {
            'name': "Nom de l'établissement",
            'adress': "Adresse",
            'city': "Ville",
            'country': "Pays",
            'study_domain': "Domaine d'étude",
        }

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        user_profile = super().save(commit=False)
        user_profile.user = user
        user_profile.user_type = 'etablissement'
        
        if commit:
            user_profile.save()
        return user_profile







class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title', 'description', 'image_url', 'study_domain']
        labels = {
            'title': "Titre de l'offre",
            'description': "Description",
            'image_url': "URL de l'image",
            'study_domain': "Domaine d'étude",
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
        }