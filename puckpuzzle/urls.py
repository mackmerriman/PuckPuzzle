from django.urls import path

from . import views

app_name = "puckpuzzle"
urlpatterns = [
    path("", views.index, name="index"),
]
