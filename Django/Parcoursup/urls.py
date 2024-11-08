from django.urls import path
from . import views
from . import views_admin
from . import views_offre
from . import views_candidature

urlpatterns = [
    # Pages principales : 
    path('home/', views.home, name='home'),  # Page principale
    path('', views.home, name='home'),  # Page principale

    # Authentification :
    path('login/', views.login_view, name='login'),  # Connexion
    path('logout/', views.logout_view, name='logout'),  # Déconnexion
    path('register_etudiant/', views.register_student, name='register_etudiant'),  # Inscription étudiant
    path('register_etablissement/', views.register_etablissement, name='register_etablissement'),  # Inscription établissement

    # Offres :
    path('offre/', views_offre.offres, name='offre'),  # Liste des offres
    path('offre/<int:offer_id>/', views_offre.offre, name='offre_id'),  # Détails d'une offre
    path('offre/create/', views_offre.offre_create, name='offre_create'),  # Créer une offre
    path('offre/show/', views_offre.offre_show, name='offre_show'),  # Montrer les offres
    path('offre/edit/<int:offer_id>/', views_offre.offre_edit, name='offre_edit'),  # Éditer une offre

    # Candidatures :
    path('candidature/', views_candidature.candidature, name='candidature'),  # Liste des candidatures
    path('gerer_candidature/<int:candidature_id>/<str:action>/', views_candidature.gerer_candidature, name='gerer_candidature'),  # Accepter ou refuser la candidature
    path('offre/<int:offer_id>/postuler/', views_candidature.postuler, name='postuler'),  # Postuler à une offre

    # Utilisateurs :
    path('profile/', views.edit_student_profile, name='profile_student'),  # Profil utilisateur


    # Admin : 
    path('admin_dashboard/', views_admin.admin_dashboard, name='admin_dashboard'),  # Tableau de bord admin
    path('admin_manage-users/', views_admin.manage_users, name='manage_users'),  # Gérer les utilisateurs
    path('admin_change-role/<int:user_id>/<str:role>/', views_admin.change_user_role, name='change_user_role'),  # Changer le rôle d'un utilisateur
    path('admin_manage-offers/', views_admin.manage_offers, name='manage_offers'),  # Gérer les offres
    path('admin_approve-offer/<int:offer_id>/<str:action>/', views_admin.approve_offer, name='approve_offer'),  # Approuver une offre
]
