from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('deconnexion/', views.logout_view, name='logout'),
]