
import random
import numpy as np
import MonteCarlo as mc

def oblicz_chi(X1, X2, X3, T, MaksL):
    Z = (MaksL * 4 + 2 * 5) / MaksL
    return Z / T * (X1 - (X2 + X3) / 2)


def stworz_lancuch(C, L, N, LL):
    for i in range(0, LL):
        for j in range(0, LL):
            for k in range(0, LL):
                L[i, j, k] = 0
    print('Tworzenie lancucha o dlugosci ', N, ' segmentow')
    built = False
    while built==False:
        built = mc._SAW(C, N, LL)
    if built:
        for i in range(0, N):
           L[int(C[i, 0]), int(C[i, 1]), int(C[i, 2])] = 1
    print('Ukonczono tworzenie lancucha')


def zmien_konformacje(Segment, LiczbaSeg, C, L, LL):
    ruch = 0
    if (Segment == 0) or (Segment == LiczbaSeg):
        if random.random() < 0.5:
            ruch = mc._reptation(Segment, LiczbaSeg, C, L, LL)
        else:
            ruch = mc._end_move(Segment, LiczbaSeg, C, L, LL)           
    else:
        if random.random() < 0.5:
            ruch = mc._crankshaft(Segment, LiczbaSeg, C, L, LL)
        else:
            ruch = mc._kink_jump(Segment, LiczbaSeg, C, L, LL)               
    return ruch


def zapisz(C, CSafe, MaksL):
    for i in range(0, MaksL):
        for j in range(0, 3):
            CSafe[i, j] = C[i, j]


def przywroc(C, CSafe, MaksL, L, LL):
    for i in range(0, MaksL):
        mc._WL(int(C[i, 0]), int(C[i, 1]), int(C[i, 2]), LL, L, 0)
    for i in range(0, MaksL):
        mc._WL(int(CSafe[i, 0]), int(CSafe[i, 1]), int(CSafe[i, 2]), LL, L, 1)
    for i in range(0, MaksL):
        for j in range(0, 3):
            C[i, j] = CSafe[i, j]


def energia(E_Seg_Seg, E_Seg_Rozp, E_Rozp_Rozp, C, MaksL, L, LL):
    freeT = 0
    CM = np.zeros((6, 3))
    for i in range(0, MaksL + 1):
        freet = mc._pusty(i, C, CM, L, LL)
        freeT += freet
    energy = freeT * E_Seg_Rozp
    energy += (MaksL * 4 + 2 - freeT) * (E_Seg_Seg + E_Rozp_Rozp) / 2
    return energy


def Odl_KK(C, MaksL):
    E_to_E = (C[0, 0] - C[MaksL, 0])**2
    E_to_E += (C[0, 1] - C[MaksL, 1])**2 + (C[0, 2] - C[MaksL, 2])**2
    return E_to_E


def ZapiszDoPliku(MaksL, ksi, srednE, EtETT, E_Seg_Seg, E_Seg_Rozp, E_Rozp_Rozp, MCNumb):
    f = open("wyniki.txt", "a")               # zapis do pliku
    line = "Liczba segmentow={0:5d}  chi={1:9.3f} srednia_energia konformacji={2:9.3f}kT  E_to_E={3:9.3f}b  PP={4:9.3f}kT  PS={5:9.3f}kT SS={6:9.3f}kT  liczba krokow MC={7:10.0f}\n"
    f.write(line.format(MaksL, ksi, srednE, EtETT, E_Seg_Seg, E_Seg_Rozp,\
        E_Rozp_Rozp, MCNumb/MaksL/4))
    f.close()
