from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signin/', views.signin_view, name='signin'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
]