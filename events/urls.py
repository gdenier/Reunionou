from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('creation/', views.New_view, name='new'),
    path('<token>/modifier/', views.Change_view, name='change'),
    path('liste/', views.List_view, name='list'),
    path('<token>/', views.Detail_view, name='detail'),
    path('inscription/<token>/', views.Register_view, name='register'),
    path('inscription/<token>/<args>/', views.Register_view, name='register'),
    path('<token>/commentaire/', views.Comment_view, name="comment"),
    path('<token>/commentaire/edit/<int:comment_id>', views.Comment_Edit_view, name="edit"),
    path('<token>/commentaire/delete/<int:comment_id>', views.Delete_com_view, name="delete_com"),
]