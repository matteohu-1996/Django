from django.urls import path
from . import views

urlpatterns = [
    # dichiariamo a django che questa app (servizio) ha un percorso di root e deve rispondere con la funzione home() del file view.py
    path("", views.home, name="home"),
    path("iscriviti", views.iscriviti, name="iscrizione")
]