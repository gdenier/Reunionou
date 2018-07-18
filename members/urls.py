from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profil/', views.profil_view, name='profil'),
    path('message/', views.message_view, name='message'),
    path('deconnexion/', views.logout_view, name='logout'),
    path('modifier/', views.change_view, name="change"),
]