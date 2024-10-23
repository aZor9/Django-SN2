from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Modèle Étudiant
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # name of user
    student_id = models.CharField(max_length=20, unique=True) #Id
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
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=127, unique=True) #mail
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
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

    def clean(self):
        if not self.is_validated:
            raise ValidationError("L'etablissement n'est pas validée.")


# Modèle Program (Programme)
class Program(models.Model):
    name = models.CharField(max_length=255)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.etablissement.is_validated:
            raise ValidationError("L'etablissement n'est pas encore validée par un administrateur.")
        super().save(*args, **kwargs)


# Modèle Application (Candidature d'étudiant à un programme)
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('rejected', 'Rejetée')
    ])

    def __str__(self):
        return f"{self.student} - {self.program} ({self.status})"


class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=200)  # Lien vers l'image
    category = models.CharField(max_length=100)  # Catégorie ou domaine
    is_approved = models.BooleanField(default=False)  # Statut de l'offre (validée ou non)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur qui a ajouté l'offre

    def __str__(self):
        return self.title
    


class OfferPro(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()  # URL pour l'image
    etablissement = models.ForeignKey('Etablissement', on_delete=models.CASCADE)  # Lien vers l'institution
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  # Pour que les admins puissent approuver les offres

    def __str__(self):
        return self.title