from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
<<<<<<< HEAD
    path('', views.home_view, name='home'),
    path('deconnexion/', views.logout_view, name='logout'),
    path('modifier/', views.change_view, name="change"),
=======
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('profil/', views.profil_view, name='profil'),
>>>>>>> 3c50f182e5f071c4735222de67880d99ecc04d54
]