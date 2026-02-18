from http.client import responses

from rest_framework import serializers
from .models import Professore, Studente, Corso, Esame


class ProfessoreSerializer(serializers.ModelSerializer):

    corsi_insegnati = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Professore
        fields = ["id", "nome", "cognome", "data_nascita", "settore", "corsi_insegnati"]


class StudenteSerializer(serializers.ModelSerializer):

    corsi_seguiti = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Studente
        fields = ["id", "nome", "cognome", "matricola", "data_nascita", "corsi_seguiti"]


class CorsoSerializer(serializers.ModelSerializer):

    numero_iscritti = serializers.SerializerMethodField()

    class Meta:
        model = Corso
        fields = ["id","codice", "nome", "crediti", "professore","numero_iscritti"]

    def get_numero_iscritti(self, obj):
        return obj.studenti.count()



class EsameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Esame
        fields = "__all__"