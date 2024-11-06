from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Offer

class StudentForm(forms.ModelForm):
    firstname = forms.CharField(required=True, label="Prénom", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Prénom"}) )
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}) )
    email = forms.EmailField(required=True, label="Adresse email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "example@mail.com"}) )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label="Mot de passe" )

    class Meta:
        model = UserProfile
        fields = ['study_domain']
        labels = {
            'study_domain': "Domaine d'étude  (A selectionner) ",
        }
        widgets = {
            'study_domain': forms.Select(attrs={'class': 'form-control'}),
        }

    field_order = ['firstname', 'username', 'email', 'password', 'study_domain']

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
    username = forms.CharField(max_length=150, required=True, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}) )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label="Mot de passe")
    email = forms.EmailField(required=True, label="Adresse email",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "example@mail.com"}) )
    name = forms.CharField(required=True, label='Nom' , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'établissement"}) )
    adress = forms.CharField(required=True, label='Adresse', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Adresse"}))
    city = forms.CharField(required=True, label='Ville', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ville"}))
    country = forms.CharField(required=True, label='Pays', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Pays"}))

    class Meta:
        model = UserProfile
        fields = ['study_domain']
        labels = {
            'study_domain': "Domaine d'étude (A selectionner)",
        }
        widgets = {
            'study_domain': forms.Select(attrs={'class': 'form-control'}),
        }

    field_order = ['username', 'name', 'email', 'password', 'study_domain', 'adress', 'city', 'country']


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
            'title': "Titre de l'offre ",
            'description': "Description ",
            'image_url': "URL de l'image ",
            'study_domain': "Domaine d'étude (A selectionner) ",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'offre'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control', 'placeholder': 'Description de l\'offre'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/image.jpg'}),
            'study_domain': forms.Select(attrs={'class': 'form-control'}),
        }


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstname', 'study_domain']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'study_domain': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = "Prénom"
        self.fields['study_domain'].label = "Domaine d'étude"