from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), #page pincipale
    path('', views.home, name='home'), #page principale

    path('login/', views.login_view, name='login'), #conexion
    path('logout/', views.logout_view, name='logout'), #deconexion
    path('register_etudiant/', views.register_student, name='register_etudiant'), #inscription etudiante
    path('register_etablissement/', views.register_etablissement, name='register_etablissement'), #inscrption etablissement


    path('propose-offer/', views.propose_offer, name='propose_offer'),

    # User
    path('offre/', views.offre, name='offre'),



    # Admin : 
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_manage-users/', views.manage_users, name='manage_users'),
    path('admin_change-role/<int:user_id>/<str:role>/', views.change_user_role, name='change_user_role'),
    path('admin_manage-offers/', views.manage_offers, name='manage_offers'),
    path('admin_approve-offer/<int:offer_id>/<str:action>/', views.approve_offer, name='approve_offer'),
]