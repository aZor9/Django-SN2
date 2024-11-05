from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Étudiant'),
        ('etablissement', 'Établissement'),
        ('admin', 'Admin'),
    ]

    STUDY_DOMAINS = [
        ('science', 'Sciences'),
        ('literature', 'Littérature'),
        ('engineering', 'Ingénierie'),
        ('arts', 'Arts'),
        ('business', 'Affaires'),
        ('medicine', 'Médecine'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    # Champs spécifiques pour les étudiants
    # date_of_birth = models.DateField(null=True, blank=True)
    firstname = models.CharField(max_length=30, null=True, blank=True)

    # Champs spécifiques pour les établissements
    name = models.CharField(max_length=255, null=True, blank=True)
    adress = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    is_validated = models.BooleanField(default=False)

    # Champs communs
    study_domain = models.CharField(
        max_length=50,
        choices=STUDY_DOMAINS,
        default='science'
    )

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"


class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    study_domain = models.CharField(
        max_length=50,
        choices=UserProfile.STUDY_DOMAINS,
        default='science'
    )
    added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Offer: {self.title} ({self.study_domain})"


class Application(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('rejected', 'Rejetée')
    ])

    def __str__(self):
        return f"Application by {self.student.user.username} for {self.offer.title} ({self.status})"
