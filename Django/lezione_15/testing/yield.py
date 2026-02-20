def genera_numeri_return():
    return [1,2,3]
    print("ciaom sono dopo il return")
print(genera_numeri_return())

def genera_numeri_yield():
    yield 1
    yield 2
    yield 3

generatore = genera_numeri_yield()
print(next(generatore)) # Next prende il prossimo valore generato dalla
# funzione yield
print(next(generatore))
print(next(generatore))

for numero in genera_numeri_yield():
    print(numero)

# esercizio 1: fare un generatore che generi i quadrati (n**2) fino a un certo n
def genera_quadrati(n: int):
    c = 0
    while c < n:
        yield c, c ** 2
        c += 1
for numero, quadrato in genera_quadrati(10):
    print(numero, quadrato)


# esercizio 2: metodo babilonese per le radici quadrate
# vogliamo calcolare la radice quadrata del numero S
# per prima cosa definiamo x_0 = S / 2
# calcoliamo x_nuovo = 0.5 * (x_precedente + S / x_precedente)
# ci fermiamo quando la differenza tra la radice calcolata con math.sqrt e il
# metodo è minore di una tolleranza data

def approssima_radice(S:int, tolleranza=1e-7):
    # facciamo il primo calcolo
    x_corrente = S / 2

    while True:
        # facciamo uscire con yield il valore x_corrente
        yield x_corrente

        # una volta ripresa la funzione, calcoliamo il necessario
        x_nuovo = 0.5 * (x_corrente + S / x_corrente)

        # controlliamo se ci dobbiamo fermare
        if abs(x_nuovo - x_corrente) < tolleranza:
            yield x_nuovo # restituiamo con yield l'ultimo valore ottenuto
            break # interrompiamo il while

        x_corrente = x_nuovo

from math import sqrt

# todo: pensiamo a una variazione in cui la tolleranza è espressa in %
numero = 126
generatore = approssima_radice(numero, tolleranza=1e-6)

print("".join("-" for _ in range(50)))
for i, stima in enumerate(generatore):
    print(f"{i + 1}, {stima}")
print(f"radice vera_ {sqrt(numero)}")