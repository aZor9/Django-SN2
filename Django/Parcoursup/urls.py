from django.urls import path
from . import views
from . import views_admin
from . import views_offre
from . import views_candidature

urlpatterns = [
    # Pages principales : 
    path('home/', views.home, name='home'), #page pincipale
    path('', views.home, name='home'), #page principale

    # Authentification :
    path('login/', views.login_view, name='login'), #conexion
    path('logout/', views.logout_view, name='logout'), #deconexion
    path('register_etudiant/', views.register_student, name='register_etudiant'), #inscription etudiante
    path('register_etablissement/', views.register_etablissement, name='register_etablissement'), #inscrption etablissement


    # Offres :
    path('offre/', views_offre.offres, name='offre'),
    path('offre/<int:offer_id>/', views_offre.offre, name='offre_id'),
    path('offre/create/', views_offre.offre_create, name='offre_create'),
    path('offre/show/', views_offre.offre_show, name='offre_show'),
    path('offre/edit/<int:offer_id>/', views_offre.offre_edit, name='offre_edit'),



    # Candidatures :
    path('candidature/', views_candidature.candidature, name='candidature'),
    path('offre/<int:offer_id>/postuler/', views_candidature.postuler, name='postuler'),
    
    
    # Utilisateurs
    path('profile/', views.profile, name='profile'),

    # Admin : 
    path('admin_dashboard/', views_admin.admin_dashboard, name='admin_dashboard'),
    path('admin_manage-users/', views_admin.manage_users, name='manage_users'),
    path('admin_change-role/<int:user_id>/<str:role>/', views_admin.change_user_role, name='change_user_role'),
    path('admin_manage-offers/', views_admin.manage_offers, name='manage_offers'),
    path('admin_approve-offer/<int:offer_id>/<str:action>/', views_admin.approve_offer, name='approve_offer'),
]