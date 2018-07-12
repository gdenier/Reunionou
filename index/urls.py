from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.Home_view, name='home'),
]