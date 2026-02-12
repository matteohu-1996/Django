from django.urls import path, include
from .views import hello_world, today_date, random_dice, random_pass, \
    verifica_palindromo, calcola_patrimonio, genera_tabellina

urlpatterns = [
    # colleghiamo a livello di APP la funzione hello_world() al percorso "hello/"
    path("hello/", hello_world, name='hello-world'),
    path("date/today", today_date, name='today-date'),
    path("random/dice", random_dice, name="dice"),
    path("random/password", random_pass, name="random-password"),
    path("verifica-palindromo", verifica_palindromo, name="verifica-palindromo"),
    path("calcola-patrimonio", calcola_patrimonio, name="calcola_patrimonio"),
    path("calcola-tabellina/<int:base>", genera_tabellina, name="genera_tabellina"),

]

# http://127.0.0.1:8000/api/v1/
