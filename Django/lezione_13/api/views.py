from rest_framework import viewsets, filters
from .models import Dispositivo, Luogo, Manutenzione, Software
from .serializers import DispositivoSerializer, LuogoSerializer, \
    ManutenzioneSerializer, SoftwareSerializer



class DispositivoViewSet(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer
    queryset = Dispositivo.objects.all()

    # 1 attiviamo i motori di filtro
    filter_backends = (filters.OrderingFilter,) # es: per ordinare

    # 2 definiamo i campi su cui possiamo svolgere una ricerca
    search_fields = ["codice", "descrizione", "luogo_nome"]


    # def get_queryset(self):
    #    queryset = Dispositivo.objects.all() # accettiamo tutti tipi di
    #    richieste
    # serializer_class = DispositivoSerializer # le facciamo passare attraverso
    # il filtro che abbiamo creato prima
        # definiamo la lettura del parametro 'luogo' dalla richiesta GET
    #    luogo_param = self.request.query_params.get('luogo', None)
        # cerchiamo di ottenere il valore del parametro, altrimenti None

        # controlliamo se è stato passato il parametro per la ricerca per luogo
    #    if luogo_param:
    #        queryset = queryset.filter(luogo__nome__icontains=luogo_param)
            # luogo__nome__icontains significa che django implicitamente per
            # le relazioni descritte nel file models.py fa una JOIN tra le
            # tabelle Dispositivi e Luoghi. Poi prende il nome del luogo e lo
            # controlla con il parametro luogo_param in modalità case
            # insensitive -> LIKE

    #    return queryset

class LuogoViewSet(viewsets.ModelViewSet):
    queryset = Luogo.objects.all()
    serializer_class = LuogoSerializer

class ManutenzioneViewSet(viewsets.ModelViewSet):
    queryset = Manutenzione.objects.all()
    serializer_class = ManutenzioneSerializer

class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

