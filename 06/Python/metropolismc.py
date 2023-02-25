
from graph import *
from MMC import *

rozm_tablicy = 100

def przyjmij_dane_startowe():
    print('Konformacja lancucha polimerowego') 
    print('Metoda: Metropolis Monte Carlo') 
    print('w trojwymiarowej przestrzeni') 
    print('__________________________________') 
    LiczbaSeg = int(input('Liczba segmentow            = ')) 
    LiczbaModyf = int(input('Liczba modyfikacji       = ')) 
    LiczbaKonf = int(input('Liczba konformacji       = ')) 
    Energia_Seg_Seg = float(input('Energia oddzialywan Segment-Segemt = ')) 
    Energia_Seg_Rozp = float(input('Energia oddzialywan Segment-Rozpuszczalnik = '))
    Energia_Rozp_Rozp = float(input('Energia oddzialywan Rozpuszczalnik-Rozpuszczalnik = '))
    return LiczbaSeg, LiczbaModyf, LiczbaKonf, Energia_Seg_Seg, Energia_Seg_Rozp, Energia_Rozp_Rozp

def symulacja_MetropolisMC():
    mc._help()
    random.seed()
    LiczbaSeg, LiczbaModyf, LiczbaKonf, Energia_Seg_Seg, Energia_Seg_Rozp,\
        Energia_Rozp_Rozp = przyjmij_dane_startowe()
    rozmiar_okna = 500
    OknoGraf = RysujOkno(rozmiar_okna) 
    T = 1; LKonf_teraz = 0; Suma_EnegriiKonf = 0; Liczba_UtworzonychKonf = 0; 
    Suma_OdlKK = 0; Liczba_OdlKK = 0
    while LKonf_teraz < LiczbaKonf:
        WspolrzWezlow = np.zeros((1000, 3))
        wspolrzedne_wezlow_kopia_zapasowa = np.zeros((1000, 3))
        L = np.zeros((rozm_tablicy, rozm_tablicy, rozm_tablicy))
        LKonf_teraz += 1
        stworz_lancuch(WspolrzWezlow, L, LiczbaSeg, rozm_tablicy)
        rysuj(OknoGraf, rozmiar_okna, WspolrzWezlow, rozm_tablicy, LiczbaSeg)
        LModyf_teraz = 0
        while LModyf_teraz < LiczbaModyf:
            Segment = random.randint(0, LiczbaSeg)
            zapisz(WspolrzWezlow, wspolrzedne_wezlow_kopia_zapasowa, LiczbaSeg)
            Energia_PoprzKonform = energia(Energia_Seg_Seg, Energia_Seg_Rozp, 
                Energia_Rozp_Rozp, WspolrzWezlow, LiczbaSeg, L, rozm_tablicy)
            metoda = zmien_konformacje(Segment, LiczbaSeg, WspolrzWezlow, L, 
                rozm_tablicy)
            if metoda != 0:
                Energia_TejKonform  = energia(Energia_Seg_Seg, Energia_Seg_Rozp, 
                    Energia_Rozp_Rozp, WspolrzWezlow, LiczbaSeg, L, rozm_tablicy)
                Pakcept = 1
                #
                #    warunek Metropolisa
                #    dla obliczenia wartosci Paccept
                #
                if (Pakcept < random.random()):               
                    przywroc(WspolrzWezlow, wspolrzedne_wezlow_kopia_zapasowa, 
                        LiczbaSeg, L, rozm_tablicy)  
                else:
                    LModyf_teraz += 1                
                if LModyf_teraz > LiczbaModyf * 3 / 4: # uklad w stanie rownowagi
                    Suma_EnegriiKonf += Energia_TejKonform
                    Liczba_UtworzonychKonf += 1
                    Suma_OdlKK += Odl_KK(WspolrzWezlow, LiczbaSeg-1)
                    Liczba_OdlKK += 1
                    print("%5d  deltaE=%5.2f/kT Odl_KK=%5.2f/b metoda=%1d" % 
                       (LModyf_teraz, (Energia_TejKonform - 
                       Energia_PoprzKonform), np.sqrt(Odl_KK(WspolrzWezlow, 
                       LiczbaSeg-1)), metoda))
                rysuj(OknoGraf, rozmiar_okna, WspolrzWezlow, rozm_tablicy, 
                       LiczbaSeg-1)
    Srednia_OdlKK = np.sqrt(Suma_OdlKK / Liczba_OdlKK)
    Srednia_EnergiaKonf = Suma_EnegriiKonf / Liczba_UtworzonychKonf
    print('Srednia energia ukladu  ', Srednia_EnergiaKonf,'kT + C')
    print('Srednia odleglosc koniec-koniec  ', Srednia_OdlKK,'b')
    print('Parametr Floryego-Hugginsa   ', oblicz_chi(Energia_Seg_Rozp, 
         Energia_Rozp_Rozp, Energia_Seg_Seg, T, LiczbaSeg))
    ZapiszDoPliku(LiczbaSeg, oblicz_chi(Energia_Seg_Rozp, Energia_Rozp_Rozp, 
         Energia_Seg_Seg, T, LiczbaSeg), Srednia_EnergiaKonf, Srednia_OdlKK, 
         Energia_Seg_Seg, Energia_Seg_Rozp, Energia_Rozp_Rozp, 
         LiczbaModyf*LiczbaKonf/LiczbaSeg*1/4)
    print('___Symulacja zakonczona___')

symulacja_MetropolisMC()
