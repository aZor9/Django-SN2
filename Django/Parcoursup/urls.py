from django.urls import path
from . import views

urlpatterns = [
    # path('', views.hello_world, name='hello_world'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'), #nouvelle page principal
    path('register/', views.register, name='register'),

    # Admin : 
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage-users/', views.manage_users, name='manage_users'),
    path('admin/change-role/<int:user_id>/<str:role>/', views.change_user_role, name='change_user_role'),
    path('admin/manage-offers/', views.manage_offers, name='manage_offers'),
    path('admin/approve-offer/<int:offer_id>/<str:action>/', views.approve_offer, name='approve_offer'),
]