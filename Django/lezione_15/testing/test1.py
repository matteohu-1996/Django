def somma(a:int, b:int):
    return a + b

# facciamo due test per la nostra funzione
def test_somma(input1, input2, corretto):
    risultato = somma(input1, input2)
    assert risultato == corretto, ("la funzione somma non ha ha dato il risultato "
                              f"sperato ({input1} + {input2} = {corretto} | "
                                   f"{risultato})")


def test_somma_multipla():
    test_somma(5, 7, 12)
    test_somma(-5, 7, 2)
    test_somma(-5, -7, -12)


# funzione area del triangolo
def area_triangolo(base: float, altezza: float):

    return (base * altezza) / 2

def test_area(base: float, altezza: float, corretto: float):
    risultato = area_triangolo(base, altezza)
    assert risultato == corretto, f"La'rea correta era {base} * {altezza} / 2 = {corretto} | {risultato}"

def test_area_multiple():
    test_area(10, 8, 40)
    test_area(3.4,19.2, 32.64)
    test_area(45, 2,45)

if __name__ == '__main__':
    test_somma_multipla()
    test_area_multiple()