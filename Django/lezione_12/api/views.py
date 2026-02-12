from django.shortcuts import render
from rest_framework.decorators import api_view # gestire i metodi HTTP e la
# comunicazione
from rest_framework.response import Response # Serializzare la risposta in
# formato HTTP
from datetime import datetime
import random

# Create your views here.
@api_view(['GET']) # come @app.get() in fastAPI ma qua non definiamo il percorso
def hello_world(request):
    # facciamo il dizionario con i dati da restituire al client
    data = {'message': 'Prima prova di un API REST in Django',
            "status": "successo"}
    # restituiamo i dati con Response
    return Response(data)

# todo: facciamo un endpoint get che restituisca un JSON con data di oggi e
#  l'ora in questo formato

@api_view(['GET'])
def today_date(request):
    today = datetime.now()
    data = {
        "giorno": today.day,
        "mese": today.month,
        "anno": today.year,
        "ora": today.hour,
        "minuto": today.minute,
    }
    return Response(data)
# collegare l'endpoint a date/today

# todo facciamo endpoint Get /random/dice che lancia due dadi da 6 facce e
#  restituisce la somma,
# se i due lanci sono uguali, alla somma aggiunge un bonus di 2 punti,
# se il bonus è aggiunto o no va segnalato nella risposta.
# La risposta avrà l'esito di ogni dado, la somma dei dadi, eventuale bonus e
# totale finale

@api_view(['GET'])
def random_dice(request):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    bonus = 2 if dice_1 == dice_2 else 0
    totale = dice_1 + dice_2 + bonus

    data = {
        "dado1": dice_1,
        "dado2": dice_2,
        "bonus": bonus,
        "somma_dadi": dice_1 + dice_2,
        "messaggio": "Complimenti, hai un bonus!" if bonus else "Mi spiace, "
                                                                "nessun bonus",
        "totale": totale
    }
    return Response(data)

# todo: facciamo una funzione che crea una password casuale di 20 caratteri,
#  che include lettere, numeri e !"%()@#+_- risponde all'endpoint
#  risponde all'endpoint random/password

# todo: Passare in post il numero di caratteri di cui fare la password,
#  dobbiamo verificare che la lunghezza rispetti un minimo di 3 caratteri
@api_view(['GET'])
def random_pass(request):
    pass_length = 20

    lettere = 'abcdefghijklmnopqrstuvwxyz'
    numeri =  '0123456789'
    speciali = '!"%()@#+_-'

    # estraiamo quanti numeri per tipo di carattere
    numero_lettere = random.randint(1, pass_length - 2)
    numero_numeri = random.randint(1, pass_length - 1 - numero_lettere)
    numero_speciali = pass_length - (numero_lettere + numero_numeri)

    #estraiamo i caratteri che compongono la nostra password
    lettere_pw = random.choices(lettere + lettere.upper(), k=numero_lettere)
    numeri_pw = random.choices(numeri, k=numero_numeri)
    speciali_pw = random.choices(speciali, k=numero_speciali)

    # mettiamo insieme le liste e le mischiamo
    caratteri_totali = lettere_pw + numeri_pw + speciali_pw
    random.shuffle(caratteri_totali)

    # concateniamo i caratteri nell'ordine ottenuto in una stringa
    password = ''.join(caratteri_totali)
    return Response({
        "password": password,
    })

# facciamo un endpoint che risponde a una richiesta POST
@api_view(['POST'])
def verifica_palindromo(request):
    """
    questa funzione prende una stringa, toglie gli spazi e verifica se la
    stringa al contrario è uguale a quella originale
    """
    # 1 dobbiamo ottenere i dati dalla richiesta
    input_utente = request.data.get('testo', "")

    # 2 se non c'è input diamo "errore"
    if not input_utente:
        return Response({"Errore": "Inserire un valore nel campo 'testo'"})

    # 3 controlliamo se la stringa, pulita dagli spazi è un palindromo
    stringa = input_utente.replace(" ", "").lower()

    # creiamo due indici destro e sinistro e vediamo se i caratteri di quei
    # indici sono diversi, se lo sono la stringa non è palindroma
    # itopinonavevanonipoti
    is_palindroma = True # di default partiamo pensando che la stringa sia
    # palindroma, vediamo se saremo smentiti
    sinistra = 0 # indice che scorre da sinistra a destra
    destra = len(stringa) - 1 # indice che scorre da destra a sinistra

    passaggi = {}

    while sinistra < destra:
        passaggi[f"passaggio_{sinistra}"] = {
            "sinistra": sinistra,
            "destra": destra,
            "carattere_sinistro": stringa[sinistra],
            "carattere_destro": stringa[destra],
            "parola_pulita": stringa,
            "lunghezza": len(stringa),
        }

        if stringa[sinistra] != stringa[destra]:
            is_palindroma = False
            break

        sinistra += 1
        destra -= 1


    return Response({
        "stringa": input_utente,
        "is_palindroma": is_palindroma,
        "pulita": stringa,
        "passaggi": passaggi,
    })

# todo: fare una funzione che prende un deposito iniziale [€], un contributo
#  mensile [€] e un tasso mensile [%]
#  restituisce l'elenco mese per mese [(02, 2026), (03, 2026), ...] del
#  valore del conto che tenga conto di incremento percentuale e
#  dell'incremento dato dal versamento mensile del regime per 30 anni

# es: conto_iniziale = 100, contributo_mensile: 10, tasso: 10%
# mese 1 (03,2026): abbiamo (100+ 10) * 1.1 = 121
# mese 2 (04,2026): abbiamo (121+ 10) * 1.1 = 144,1

@api_view(['POST'])
def calcola_patrimonio(request):
    date = datetime.now()
    mese, anno = date.month + 1, date.year

    anni = 30
    mesi_durata = anni + 12

    capitale_iniziale = request.data.get('capitale_iniziale', None)
    contributo_mensile = request.data.get('contributo_mensile', None)
    tasso = request.data.get('tasso', None) / 100 # cosi otteniamo
    # direttamente il coefficiente che ci piace

    # bisogna ancora inizilizzare/creare le variabili da usare per i soldi
    data = {
        "mesi": [],
        "patrimonio_iniziale": capitale_iniziale,
        "tasso": tasso,
        "contributo_mensile": contributo_mensile,
        "totale_versato": contributo_mensile * anni * mesi_durata,
        # opzionale si può mettere lo scarto tra versato e guadagnato
        "totale": 0
    }
    for mese_corrente in range(mese, mesi_durata + mese):
        mese_corrente += mese
        mese_convertito = mese_corrente % 12
        anno_convertito = mese_corrente // 12 + anno

        patrimonio_iniziale = data["totale"]
        patromonio = patrimonio_iniziale + contributo_mensile
        patromonio_fine_mese = patromonio * (1 + tasso)

        row = {
            "id": f"{mese_convertito}, {anno_convertito}",
            "patrimonio": ...
        }

        data["totale"] = patromonio_fine_mese
        data["mesi"].append(row)

    return Response(data)

# il numero di cui calcolare la tabellina verrà poi passato attraverso la
# path dell'endpoint
# fastAPI scrivevamo @app.get("/percorso/{numero}")
# NB: la tipologia della variabile in fastAPI la avremo scritta nella
# dichiarazione della funzione
# def funzione(..., numero:int)
@api_view(['GET'])
def genera_tabellina(request, base):
    tabellina = [base * i for i in range(1,11)]
    return Response({
        "numero": base,
        "tabellina": tabellina,
        "formula": f"{base} * n, con n = 1, ..., 10"
    })

@api_view(['GET'])
def mini_calc(request):
    # es di richiesta: path/mini-calc?a=n&b=M
    # senza la "&" avremo solo un parametro a con il valore "Nb=M"
    # convertendo la query in path avremmo avuto:
    # path/mini-calc/<float:a>/<float:b>

    OPERAZIONI = {"sum", "sub", "mol", "div"}

    try:
        num_a = float(request.data.get('a', 0))
        num_b = float(request.data.get('b', 0))
        operazione = request.data.get('operazione', "")

        if operazione not in OPERAZIONI:
            return Response({"errore": f"l'operazione deve essere una tra "
                                       f"{OPERAZIONI}"}, status=400)
        if operazione == "div" and num_b == 0:
            return Response({"errore": "Non si può dividere per 0"}, status=400)

        if operazione == "sum":
            risultato = num_a + num_b
        elif operazione == "sub":
            risultato = num_a - num_b
        elif operazione == "mol":
            risultato = num_a * num_b
        else:
            risultato = num_a / num_b

        return Response({
            "operazione": f"Operazione da fare: {operazione}",
            "a": num_a,
            "b": num_b,
            "totale": risultato,
        })


    except ValueError:
        return Response({
            "Errore": "Uno tra a e b (o entrambi, non è un numero",
            "a_ottenuto": request.data.get("a", None ),
            "b_ottenuto": request.data.get("b", None),
        })

















