import random
import numpy as np

def _help():
    print('MonteCarlo.py')
    print('======================================')
    print('lista funkcji: _pusty, _SAW, _end_move')
    print('_reptation, _crankshaft, _kink_jump   ')
    print('_RL, _WL -periodyczne warunki brzegowe')
    print('======================================')
    
def _RL(x,y,z,C,LL,L): 
    LL=LL-1
    while x<0:
        x+=LL
    while y<0:
        y+=LL
    while z<0:
        z+=LL   
    while x>LL:
        x-=LL
    while y>LL:
        y-=LL
    while z>LL:
        z-=LL  
    return L[x,y,z] 

def _WL(x,y,z,LL,L,W): 
    LL=LL-1
    while x<0:
        x+=LL
    while y<0:
        y+=LL
    while z<0:
        z+=LL   
    while x>LL:
        x-=LL
    while y>LL:
        y-=LL
    while z>LL:
        z-=LL  
    L[x,y,z]=W    
    
    
def warunki_SAW(C, N):
    kolizja = False
    for k in range(0, N):
        if C[N, 0] == C[k, 0] and C[N, 1] == C[k, 1] and C[N, 2] == C[k, 2]:
            kolizja = True
    return kolizja


def _SAW(C, N, LL):
    C[0, 0] = int(LL / 2)
    C[0, 1] = int(LL / 2)
    C[0, 2] = int(LL / 2)
    for j in range(1, N + 1):      
        zwrot = 2 * random.randint(0, 1) - 1
        dir = random.randint(0, 2)
        for k in range(0, 3):
            C[j, k] = C[j - 1, k]
        C[j, dir] += zwrot
        uciekaj = 0
        while warunki_SAW(C, j):
            zwrot = 2 * random.randint(0, 1) - 1
            dir = random.randint(0, 2)
            for k in range(0, 3):
                C[j, k] = C[j - 1, k]
            C[j, dir] += zwrot
            uciekaj += 1
            if uciekaj > 100:
                return False
    return True


def _pusty(N, C, CM, L, LL):
    f = -1
    x = int(C[N, 0]); y = int(C[N, 1]); z = int(C[N, 2])
    if _RL(x, y, z + 1, C, LL, L)==0:
        f += 1; CM[f, 0] = x; CM[f, 1] = y; CM[f, 2] = z + 1
    if _RL(x, y, z - 1, C, LL, L)==0:
        f += 1; CM[f, 0] = x; CM[f, 1] = y; CM[f, 2] = z - 1
    if _RL(x, y + 1, z, C, LL, L)==0:
        f += 1; CM[f, 0] = x; CM[f, 1] = y + 1; CM[f, 2] = z
    if _RL(x, y - 1, z, C, LL, L)==0:    
        f += 1; CM[f, 0] = x; CM[f, 1] = y - 1; CM[f, 2] = z
    if _RL(x + 1, y, z, C, LL, L)==0:
        f += 1; CM[f, 0] = x + 1; CM[f, 1] = y; CM[f, 2] = z
    if _RL(x - 1, y, z, C, LL, L)==0:    
        f += 1; CM[f, 0] = x - 1; CM[f, 1] = y; CM[f, 2] = z
    return f


def _end_move(N, N1, C, L, LL):
    CM = np.zeros((6, 3)) 
    if N == 0:
        NH = N + 1       
        mov = _pusty(NH, C, CM, L, LL)
        if mov < 2:
            return 0
    else:    
        NH = N - 2
        mov = _pusty(NH, C, CM, L, LL)
        if mov < 2:
            return 0
    mov1 = random.randint(0, mov)  
    if N != 0:
        N-=1  
    _WL(int(C[N, 0]), int(C[N, 1]), int(C[N, 2]), LL, L, 0)        
    C[N, 0] = CM[mov1, 0]
    C[N, 1] = CM[mov1, 1]
    C[N, 2] = CM[mov1, 2]
    _WL(int(C[N, 0]), int(C[N, 1]), int(C[N, 2]), LL, L, 1)
    return 1


def _reptation(N, Mx, C, L, LL):
    CM = np.zeros((6, 3))
    N1 = Mx - 1
    N2 = 0
    if random.random() < 0.5:
        N1 = 0
        N2 = Mx - 1  
    mov = _pusty(N1, C, CM, L, LL)
    if mov < 2:
        return 0   
    mov1 = random.randint(0, mov)
    if _RL(int(CM[mov1, 0]), int(CM[mov1, 1]), int(CM[mov1, 2]), C, LL, L)!=0:
        return 0 
    _WL(int(C[N2, 0]), int(C[N2, 1]), int(C[N2, 2]), LL, L, 0)        
    if N1 == 0:
        for i in range(Mx - 1, 0, -1):
            C[i, 0] = C[i - 1, 0]
            C[i, 1] = C[i - 1, 1]
            C[i, 2] = C[i - 1, 2]
        C[0, 0] = CM[mov1, 0]
        C[0, 1] = CM[mov1, 1]
        C[0, 2] = CM[mov1, 2]
    else:
        for i in range(0, Mx):
            C[i, 0] = C[i + 1, 0]
            C[i, 1] = C[i + 1, 1]
            C[i, 2] = C[i + 1, 2]
        C[Mx - 1, 0] = CM[mov1, 0]
        C[Mx - 1, 1] = CM[mov1, 1]
        C[Mx - 1, 2] = CM[mov1, 2]
    for i in range(0, Mx):  
        _WL(int(C[i,0]),int(C[i,1]),int(C[i,2]), LL, L, 1)
    return 2


def _crankshaft(N, MaksL, C, L, LL):
    CM1 = np.zeros((6, 3))
    CM2 = np.zeros((6, 3))
    Nmin = N
    Nmaks = N + 3
    if (Nmaks > MaksL - 2):
        return 0
    ix = -1
    for i in range(0, 3):
        if (C[Nmin, i] == C[Nmin + 1, i]) and \
           (C[Nmin, i] == C[Nmin + 2, i]) and \
           (C[Nmin, i] == C[Nmin + 3, i]):
            ix = i
    if ix == -1:
        return 0
    iy = -1
    if (C[Nmin, 0] == C[Nmaks, 0] + 1) and \
       (C[Nmin, 1] == C[Nmaks, 1]) and \
       (C[Nmin, 2] == C[Nmaks, 2]):
        iy = 0
    if (C[Nmin, 0] == C[Nmaks, 0] - 1) and \
       (C[Nmin, 1] == C[Nmaks, 1]) and \
       (C[Nmin, 2] == C[Nmaks, 2]):
        iy = 0
    if (C[Nmin, 0] == C[Nmaks, 0]) and \
       (C[Nmin, 1] == C[Nmaks, 1] + 1) and \
       (C[Nmin, 2] == C[Nmaks, 2]):
        iy = 1
    if (C[Nmin, 0] == C[Nmaks, 0]) and \
       (C[Nmin, 1] == C[Nmaks, 1] - 1) and \
       (C[Nmin, 2] == C[Nmaks, 2]):
        iy = 1
    if (C[Nmin, 0] == C[Nmaks, 0]) and \
       (C[Nmin, 1] == C[Nmaks, 1]) and \
       (C[Nmin, 2] == C[Nmaks, 2] + 1):
        iy = 2
    if (C[Nmin, 0] == C[Nmaks, 0]) and \
       (C[Nmin, 1] == C[Nmaks, 1]) and \
       (C[Nmin, 2] == C[Nmaks, 2] - 1):
        iy = 2
    if iy == -1:
        return 0
    iz = -1    
    for i in range(0, 3):
        if (i != ix) and (i != iy):
            iz = i
    for j in range(0, 3):
        for i in range(0, 3):
            CM1[j, i] = C[Nmin + 1, i]
        for i in range(0, 3):
            CM2[j, i] = C[Nmin + 2, i]
    CM1[0, iz] = C[Nmin, iz]; CM1[0, ix] = C[Nmin, ix] + 1
    CM2[0, iz] = C[Nmin, iz]; CM2[0, ix] = C[Nmin, ix] + 1
    CM1[1, iz] = C[Nmin, iz]; CM1[1, ix] = C[Nmin, ix] - 1
    CM2[1, iz] = C[Nmin, iz]; CM2[1, ix] = C[Nmin, ix] - 1
    CM1[2, iz] = 2 * C[Nmin, iz] - CM1[2, iz]
    CM2[2, iz] = 2 * C[Nmin, iz] - CM2[2, iz]
    t = random.randint(0, 2)
    if _RL(int(CM1[t, 0]), int(CM1[t, 1]), int(CM1[t, 2]), C, LL, L)==0 and \
       _RL(int(CM2[t, 0]), int(CM2[t, 1]), int(CM2[t, 2]), C, LL, L)==0:
        _WL(int(C[Nmin + 1, 0]), int(C[Nmin + 1, 1]), int(C[Nmin + 1, 2]), LL, L, 0)
        _WL(int(C[Nmin + 2, 0]), int(C[Nmin + 2, 1]), int(C[Nmin + 2, 2]), LL, L, 0)
        C[Nmin+1,0]=CM1[t,0]
        C[Nmin+1,1]=CM1[t,1]
        C[Nmin+1,2]=CM1[t,2]
        C[Nmin+2,0]=CM2[t,0]
        C[Nmin+2,1]=CM2[t,1]
        C[Nmin+2,2]=CM2[t,2]
        _WL(int(CM1[t, 0]), int(CM1[t, 1]), int(CM1[t, 2]), LL, L, 1)
        _WL(int(CM2[t, 0]), int(CM2[t, 1]), int(CM2[t, 2]), LL, L, 1)       
    return 3


def _kink_jump(N, Maks, C, L, LL):
    CM1 = np.zeros((6, 3))
    CM2 = np.zeros((6, 3))
    CM3 = np.zeros((6, 3))
    if random.random() > 0.5:
        N1 = N + 2
    else:
        N1 = N - 2
    if (N1 > Maks) or (N1 < 0):
        return 0
    mov1 = _pusty(N, C, CM1, L, LL)
    mov2 = _pusty(N1, C, CM2, L, LL)
    k = 0
    for i in range(0, mov1):
        for j in range(0, mov2):
            if CM1[i, 0] == CM2[j, 0] and CM1[i, 1] == CM2[j, 1] and CM1[i, 2] == \
                   CM2[j, 2]:
                k += 1
                CM3[k, 0] = CM1[i, 0]
                CM3[k, 1] = CM1[i, 1]
                CM3[k, 2] = CM1[i, 2]
    if k == 0:
        return 0
    else:
        k1 = random.randint(1, k)
        NC = (N + N1) // 2
        _WL(int(C[NC, 0]), int(C[NC, 1]), int(C[NC, 2]), LL, L, 0)
        C[NC, 0] = CM3[k1, 0]
        C[NC, 1] = CM3[k1, 1]
        C[NC, 2] = CM3[k1, 2]
        _WL(int(C[NC, 0]), int(C[NC, 1]), int(C[NC, 2]), LL, L, 1)
    return 4
