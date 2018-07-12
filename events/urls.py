from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('user/<int:user_id>/new/', views.New_view, name='new'),
    path('<int:event_id>/change/', views.Change_view, name='change'),
    path('list/', views.List_view, name='list'),
    path('<token>/', views.Detail_view, name='detail'),
    path('inscription/<token>', views.Inscription_view, name='inscription'),
    path('inscription/<token>/<args>', views.Inscription_view, name='inscription'),
]