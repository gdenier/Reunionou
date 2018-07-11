from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('user/<int:user_id>/new/', views.New_view, name='new'),
]