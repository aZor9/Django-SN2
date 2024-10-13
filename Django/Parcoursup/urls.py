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
]