import random
from graph_4 import *


def warunki_NRRW(x, y, x2, y2, N):
    zderzenie = False
    #   warunki NRRW
    #
    return zderzenie

def warunki_SAW(x, y, x2, y2, N):
    zderzenie = False
    #   warunki SAW
    #   biezacy segment: Liczba
    #         x, y
    return zderzenie


def bladzenie_przypadkowe(MaksDlLancucha, OdlKwadr, IleLancuchow):
    x, y = [0], [0]
    przesuniecie = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for Liczba in range(1, MaksDlLancucha):
        skok_x, skok_y = przesuniecie[random.randint(0, 3)]
        x2 = x[Liczba - 1] + skok_x
        y2 = y[Liczba - 1] + skok_y

        while warunki_NRRW(x, y, x2, y2, Liczba):
            skok_x, skok_y = przesuniecie[random.randint(0, 3)]
            x2 = x[Liczba - 1] + skok_x
            y2 = y[Liczba - 1] + skok_y
        # *********************************************************
        if warunki_SAW(x, y, x2, y2, Liczba):
            break
        else:
            x.append(x[Liczba - 1] + skok_x)
            y.append(y[Liczba - 1] + skok_y)
            OdlKwadr[Liczba] += x[Liczba] ** 2 + y[Liczba] ** 2
            IleLancuchow[Liczba] += 1
    # *********************************************************
    return x, y, OdlKwadr, IleLancuchow
def lancuch(OknoGraf, rozmiar_okna, MaksDlLancucha, OdlKwadr, IleLancuchow):
    x, y, OdlKwadrat, IleLancuchow = bladzenie_przypadkowe(MaksDlLancucha, OdlKwadr, IleLancuchow)
         # generowanie pojedynczego lancucha
    rysuj(OknoGraf, rozmiar_okna, x, y, len(x))
    return OdlKwadrat, IleLancuchow

def symulacja():
    start_generatora = int(input("Liczba startowa generatora  = "))
    LiczbaKonformacji = int(input("Liczba konformacji = "))
    rozmiar_okna = 500
    OknoGraf=rysujOkno(rozmiar_okna)
    if start_generatora != 0:
        random.seed(start_generatora, 2)
    else:
        random.seed()
    MaksDlLancucha = 1000
    OdlKwadr = [0]
    IleLancuchow = [0]
    for i in range(0, MaksDlLancucha):   # inicjowanie list wynikow
        OdlKwadr.append(0)
        IleLancuchow.append(0)
    for j in range(LiczbaKonformacji):      # glowna symulacja
        lancuch(OknoGraf, rozmiar_okna, MaksDlLancucha, OdlKwadr, IleLancuchow)
    for i in range(0, MaksDlLancucha):   # obliczenia koncowe
        if IleLancuchow[i] != 0:
            OdlKwadr[i] = OdlKwadr[i] / IleLancuchow[i]
    OknoGraf.close()
    f = open("wyniki.txt", "w")    # zapis do pliku
    linia = "{0:5d}  {1:9.3f}  {2:5d}\n"
    for i in range(1, MaksDlLancucha):
        if IleLancuchow[i] != 0:
            f.write(linia.format(i, OdlKwadr[i], IleLancuchow[i]))
    f.close()
    print("Program został wykonany")

symulacja()