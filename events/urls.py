from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('nouveau/', views.New_view, name='new'),
    path('<token>/modifier/', views.Change_view, name='change'),
    path('liste/', views.List_view, name='list'),
    path('<token>/', views.Detail_view, name='detail'),
    path('inscription/<token>/', views.Register_view, name='register'),
    path('inscription/<token>/<args>/', views.Register_view, name='register'),
    path('<token>/commentaire/', views.Comment_view, name="comment"),
    path('<token>/commentaire/edit/<int:comment_id>', views.Comment_Edit_view, name="edit"),
    path('<token>/commentaire/delete/<int:comment_id>', views.Delete_com_view, name="delete_com"),
    path('<token>/commentaire/like/<int:comment_id>', views.Like_com_view, name="like_com"),
    path('<token>/commentaire/dislike/<int:comment_id>', views.Dislike_com_view, name="dislike_com"),
    path('ajax/getsetevent/', views.getSetPos, name='setPos'),
]