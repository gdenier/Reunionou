from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('connexion/', views.login_view, name='login'),
    path('inscription/', views.register_view, name='register'),
    path('', views.Home_view, name='home'),
]