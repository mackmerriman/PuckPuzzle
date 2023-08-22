from django.urls import path

from . import views

app_name = "puckpuzzle"
urlpatterns = [
    path("", views.index, name="index"),
    path("api/search", views.filterPlayers, name="api_search"),
    path("api/check", views.checkPlayer, name="api_check"),
    path('tasks/create_daily_game/', views.run_daily_game_creation,
         name='run_daily_game_creation'),
]
