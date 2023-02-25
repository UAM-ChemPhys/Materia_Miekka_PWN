import random
from numpy import *
from graph import *

L = 100
StepMax = 100000
MaxAutoC = 5000
C = zeros((StepMax + 1, 3))
Signal = zeros((StepMax + 1))
AutoC = zeros((MaxAutoC + 1))


def start():
    print('Symulacja eksperymentu DLS')
    print('________________________________')
    print('Rozmiar pudla symulacyjnego = ', L)
    Box = int(input('Rozmiar pudla analitycznego = '))
    Dis = int(input('Srednie przesuniecie        = '))
    Nmax = int(input('Liczba czastek              = '))
    Tstep = int(input('Krok czasu                  = '))
    name = str(input('Nazwa pliku wynikow         = '))
    for i in range(1, Nmax):
        C[i, 0] = (1 - 2 * random.random()) * L
        C[i, 1] = (1 - 2 * random.random()) * L
        C[i, 2] = (1 - 2 * random.random()) * L
    return Box, Dis, Nmax, Tstep, name


def NewLocation(N, Dis):
    fi = pi * random.random()
    theta = 2 * pi * random.random()
    R = 0
    for i in range(1, 13):
        R += random.random()
    R = 2 * Dis * (R - 6)
    C[N, 0] += R * cos(fi) * cos(theta)
    C[N, 1] += R * cos(fi) * sin(theta)
    C[N, 2] += R * sin(fi)


def PeriodicBoundaries(N):
    for i in range(0, 3):
       if C[N, i] < -L:
           C[N, i] = C[N, i]+2 * L
       if C[N, i] > L:
           C[N, i] = C[N, i]-2 * L


def Check(mode, Nmax, Box, C):
    lambda1 = 10
    intensity = 0
    for i in range(1, Nmax + 1):
        if (C[i, 0] > -Box) and (C[i, 0] < Box):
            if (C[i, 1] > -Box) and (C[i, 1] < Box):
                if (C[i, 2] > -Box) and (C[i, 2] < Box):
                    if mode == 1:
                        intensity += 1
                    else:
                        intensity += sin(C[i, 2] / lambda1)
    if mode == 1:
        Check1 = intensity
    else:
        Check1 = intensity ** 2
    return Check1


def DLS():
    random.seed()
    Box, Dis, Nmax, Tstep, name = start()
    name1 = 'signal_' + name
    Step = 0
    Signal[Step] = 0
    T = 0
    TT = 0
    Tmax = StepMax * Tstep
    dim1 = 800
    dim2 = 300
    win = draw0(dim1, dim2)
    while T < Tmax:
        T += 1
        TT += 1
        N = random.randint(0, Nmax + 1)
        NewLocation(N, Dis)
        PeriodicBoundaries(N)
        if TT == Tstep:
            TT = 0
            Step += 1
            if Step > StepMax:
                break
            else:
                Signal[Step] = Check(1, Nmax, Box, C)              # rozwaz 0 dla trybu interferencji
                print(T, '   ', Signal[Step])
                draw1(win, dim1, dim2, Step - 1, Step, Signal[Step - 1], Signal[Step], StepMax, Nmax * power(Box / L, 3))
    AutoCN = 0
                          # obliczanie funkcji autokorelacyjnej
                          # z rejestru przesunwego
                          # tablica funkcji autokorelacyjnej:
                          # AutoC:array[1..MaxAutoC]
                          # liczba zliczen
                          # AutoCN (counter)
    for i in range(0, MaxAutoC):
        if AutoCN != 0:
            AutoC[i] = (AutoC[i] / AutoCN) * (Nmax * power(Box / L, 3) ** 2)
    f = open(name1, "w")                                  # zapis do pliku
    line = "{0:10d}  {1:9.3f}\n"
    for i in range(0, StepMax):
        f.write(line.format(i, Signal[i]))
    f.close()
    f = open(name, "w")                                   # zapis do pliku
    line = "{0:10d},  {1:12.9f}\n"
    A = 20
    for i in range(1, MaxAutoC // A):
        f.write(line.format(i * Tstep * A, AutoC[i * A]))
    f.close()
    print('Program zostal wykonany')

DLS()
