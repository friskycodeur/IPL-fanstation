from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerListView.as_view(), name='player_list'),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name='player_detail'),
    path('player/new/', views.CreatePlayerView.as_view(), name='player_new'),
    path('player/<int:pk>/edit/',
         views.UpdatePlayerView.as_view(), name='player_edit'),
    path('player/<int:pk>/remove/',
         views.PlayerDetailView.as_view(), name='player_remove'),
    path('player/<int:pk>/publish/',
         views.player_publish, name='player_publish'),
]
