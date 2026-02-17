from http.client import responses

from rest_framework import serializers
from .models import Dispositivo, Luogo, Manutenzione, Software


class LuogoSerializer(serializers.ModelSerializer):
    numero_dispositivi = serializers.SerializerMethodField()

    class Meta:
        model = Luogo
        # fields = '__all__' # prende tutti i campi disponibili
        fields = ['id', 'nome', 'piano', 'note', 'numero_dispositivi']

    def get_numero_dispositivi(self, obj):
        return obj.dispositivi.count()


class ManutenzioneSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manutenzione
        fields = '__all__'


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'



class DispositivoSerializer(serializers.ModelSerializer):
    # dobbiamo spiegare a django che le colonne costo_totale e
    # numero_interventi sono calcolate e non nel DB
    # NB: "costo_totale" deve essere lo stesso nome che usiamo per
    # l'attributo nella classe, nome della colonna e sotto in get_ATTRIBUTO()
    # = get_costo_totale()
    costo_totale = serializers.SerializerMethodField()
    numero_interventi = serializers.SerializerMethodField()
    numero_software = serializers.SerializerMethodField()

    class Meta:
        model = Dispositivo
        fields = [
            'id', 'codice', 'descrizione', 'luogo',
            'software_installati',
            'numero_software',
            'stato_operativo',
            'costo_totale',
            'numero_interventi',
        ]
        # depth = 1 # utile solamente per serializer di sola lettura

    # questa funzione viene chiamata solamente per restituire i dati dal DB,
    # quindi quando vogliamo scrivere i dati nel db, django si comporta come
    # sempre, come se questa funzione non esistesse
    def to_representation(self, instance):
        # 1 otteniamo la rappresentazione standard (cioè quella con ID di
    # tutto e non i dati annidati)
        response = super().to_representation(instance) # chiamiamo il metodo
        # originale presente nella classe serializers.ModelSerializer

        # 2 sostituiamo l'id del luogo con l'oggetto completo
        if instance.luogo: # controlliamo se c'è, perchè potrebbe essere null
            response['luogo'] = LuogoSerializer(instance.luogo).data

        # 3 facciamo lo stesso per i software
        # siccome software_installati è una lista, possiamo non fare IF
        response['software_installati'] = SoftwareSerializer(
            instance.software_installati.all(), many=True).data
        return response



    def get_costo_totale(self, obj):
        # obj è l'istanza attuale del Dispositivo, da non confondere con il
# DispositivoSerializer che invece è "l'insieme di regole per utilizzare gli
# oggetti di classe "Dispositivo"

        interventi = obj.manutenzioni.all() # otteniamo tutte le manutenzioni
        # fatte su questo Dispositivo
        return sum(intervento.costo for intervento in interventi)

    def get_numero_interventi(self, obj):
        return obj.manutenzioni.count()

    def get_numero_software(self, obj):
        return obj.software_installati.count()