from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Modèle Étudiant
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # name of user
    student_id = models.CharField(max_length=20) #Id
    date_of_birth = models.DateField() # date de naissance
    # high_school = models.CharField(max_length=200) #lycée
    firstname = models.CharField(max_length=30) #prenom
    email = models.EmailField(max_length=127, unique=True) #mail

    # Liste prédéfinie de domaines d'études
    STUDY_DOMAINS = [
        ('science', 'Science'),
        ('literature', 'Literature'),
        ('engineering', 'Engineering'),
        ('arts', 'Arts'),
        ('business', 'Business'),
        ('medicine', 'Medicine'),
    ]

    study_domain = models.CharField(
        max_length=50,
        choices=STUDY_DOMAINS,
        default='science'  # Valeur par défaut
    )


    def __str__(self):
        return f"{self.user.username} ({self.student_id})"




# Modèle Etablissement (Établissement)
class Etablissement(models.Model):
    name = models.CharField(max_length=255, default= 'name')
    email = models.EmailField(max_length=127 , default= 'email@email.com') #mail
    adress = models.CharField(max_length=200, default= 'adress')
    city = models.CharField(max_length=100, default= 'city')
    country = models.CharField(max_length=100, default=' country')
    is_validated = models.BooleanField(default=False)  

    # Liste prédéfinie de domaines d'études
    STUDY_DOMAINS = [
        ('science', 'Science'),
        ('literature', 'Literature'),
        ('engineering', 'Engineering'),
        ('arts', 'Arts'),
        ('business', 'Business'),
        ('medicine', 'Medicine'),
    ]

    study_domain = models.CharField(
        max_length=50,
        choices=STUDY_DOMAINS,
        default='science'  # Valeur par défaut
    )

    
    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.TextField(max_length=100000)  # Lien vers l'image
    category = models.CharField(max_length=100)  # Catégorie ou domaine
    is_approved = models.BooleanField(default=False)  # Statut de l'offre (validée ou non)
    added_by = models.ForeignKey(Etablissement, on_delete=models.CASCADE)  # Utilisateur qui a ajouté l'offre

    def __str__(self):
        return self.title
    
# Modèle Application (Candidature d'étudiant à un programme)
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('rejected', 'Rejetée')
    ])

    def __str__(self):
        return f"{self.student} - {self.program} ({self.status})"
