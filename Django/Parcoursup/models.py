from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lien vers l'utilisateur
    date_of_birth = models.DateField()
    firstname = models.CharField(max_length=30)

    STUDY_DOMAINS = [
        ('science', 'Sciences'),
        ('literature', 'Littérature'),
        ('engineering', 'Ingénierie'),
        ('arts', 'Arts'),
        ('business', 'Affaires'),
        ('medicine', 'Médecine'),
    ]

    study_domain = models.CharField(
        max_length=50,
        choices=STUDY_DOMAINS,
        default='science'
    )

    def __str__(self):
        return f"{self.user.username} ({self.firstname})"


class Etablissement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lien vers l'utilisateur
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_validated = models.BooleanField(default=False)

    STUDY_DOMAINS = [
        ('science', 'Sciences'),
        ('literature', 'Littérature'),
        ('engineering', 'Ingénierie'),
        ('arts', 'Arts'),
        ('business', 'Affaires'),
        ('medicine', 'Médecine'),
    ]

    study_domain = models.CharField(
        max_length=50,
        choices=STUDY_DOMAINS,
        default='science'
    )

    def __str__(self):
        return f"{self.name} ({self.city})"


class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=500)  # Utilisation d'URLField pour les URL
    study_domain = models.CharField(
        max_length=50,
        choices=Etablissement.STUDY_DOMAINS,
        default='science'
    )
    added_by = models.ForeignKey(Etablissement, on_delete=models.CASCADE)

    def __str__(self):
        return f"Offer: {self.title} ({self.study_domain})"


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
        return f"Application by {self.student.user.username} for {self.offer.title} ({self.status})"


class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Étudiant'),
        ('etablissement', 'Établissement'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
