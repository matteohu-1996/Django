from django.db import models

class Professore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()
    settore = models.CharField(max_length=100)

    def __str__(self):
        return f"Prof. {self.cognome} {self.nome}"


class Studente(models.Model):
    matricola = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()


    def __str__(self):
        return f"{self.cognome} {self.nome} - {self.matricola}"



class Corso(models.Model):
    codice = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    crediti = models.IntegerField(default=6)

    def __str__(self):
        return f"{self.codice} {self.nome}"


    professore = models.ForeignKey(Professore, on_delete=models.SET_NULL, null=True, related_name='corsi_insegnati')
    # mettiamo null perchè i corsi dell'università esistono a prescindere da chi li insegna, eliminato un professore, il corso verrà assegnato a qualcun'altro

    # N:N -> Django genera automaticamente una tabella nel DB per gestire questa relazione
    studenti = models.ManyToManyField(Studente, blank=True,related_name='corsi_seguiti')

class Esame(models.Model):
    id = models.IntegerField(primary_key=True)
    data_ora = models.DateTimeField()

    def __str__(self):
        return f"Esame ID: {self.id}"

