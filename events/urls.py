from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('new/', views.New_view, name='new'),
    path('<token>/change/', views.Change_view, name='change'),
    path('list/', views.List_view, name='list'),
    path('<token>/', views.Detail_view, name='detail'),
    path('inscription/<token>', views.Inscription_view, name='inscription'),
    path('inscription/<token>/<args>', views.Inscription_view, name='inscription'),
]