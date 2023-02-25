import random
import numpy as np
from graph import *
import matplotlib.pyplot as plt


def start(Nconf, Nsegm, RNumb):
    Nconf = int(input('Liczba konformacji = '))
    Nsegm = int(input('Liczba segmentow   =      '))
    RNumb = int(input('Random number seed =      '))
    return Nconf, Nsegm, RNumb


def Entropy():
    print('3D generator SAW')
    print('________________')
    segment = 1
    Nconf = 0
    Nsegm = 0
    RNumb = 0
    Nconf, Nsegm, RNumb = start(Nconf, Nsegm, RNumb)
    dim = 500
    win = draw0(dim)
    L = 600
    V = np.zeros((L, L, L))
    C = np.zeros((Nsegm, 3))
    S = np.zeros((Nsegm))
    omega = np.zeros((Nsegm, 2))
    if RNumb != 0:
        random.seed(RNumb, 2)
    else:
        random.seed()
    for i in range(0, Nconf):
        C[0, 0] = int(L/2)
        C[0, 1] = int(L/2)
        C[0, 2] = int(L/2)
        omega[0, 0] = omega[0, 0] + np.log(6)
        omega[0, 1] += 1
        for j in range(1, Nsegm):
            turn = 2 * random.randint(0, 1) - 1
            dir = random.randint(0, 2)
            for k in range(0, 3):
                C[j, k] = C[j - 1, k]
            C[j, dir] += turn
            x = int(C[j, 0])
            y = int(C[j, 1])
            z = int(C[j, 2])
            if V[x, y, z] == 0:
                V[x, y, z] = segment
                #
                #  obliczenia entropii
                #
            else:
                for k in range(0, j):
                   V[int(C[k, 0]), int(C[k, 1]), int(C[k, 2])] = 0
                break
        draw1(win, dim, L, C, j - 1)
    for j in range(0, Nsegm):                                   # obliczenia koncowe
        if omega[j, 1] != 0:
            omega[j, 0] = omega[j, 0] / omega[j, 1]
    for i in range(0, Nsegm):
        for j in range(0, i):
            S[i] += omega[j, 0]
    f = open("wyniki.txt", "w")                                 # zapis do pliku
    line = "{0:5d},  {1:9.3f},  {2:9.3f},  {3:9.3f}\n"
    for j in range(1, Nsegm):
        if omega[j, 1] != 0:
            f.write(line.format(j, omega[j, 1], np.exp(omega[j, 0]), S[j]))
    f.close()
    print('Program zostal wykonany')


Entropy()
