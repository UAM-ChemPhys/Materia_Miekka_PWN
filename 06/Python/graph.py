
from graphics import *


def RysujOkno(dim):
    win = GraphWin('Bladzenie przypadkowe', dim, dim)
    win.setCoords(0, 0, dim - 1, dim - 1)
    return win


def rysuj(win, dim, C, edge, ML):
    asp = 10
    L = [0]
    p1 = 1
    p2 = 2
    p3 = 0
    shift=0.3
    E=edge/2
    for i in range(ML):
        L.append(0)
    for i in range(ML):
        x1 = int((C[i,p1]-E+(C[i,p3]-E)*shift)*asp+dim/2)
        y1 = int((C[i,p2]-E+(C[i,p3]-E)*shift)*asp+dim/2)
        x2 = int((C[i+1,p1]-E+(C[i+1,p3]-E)*shift)*asp+dim/2)
        y2 = int((C[i+1,p2]-E+(C[i+1,p3]-E)*shift)*asp+dim/2)
        L[i] = Line(Point(x1, y1), Point(x2, y2))
        L[i].draw(win)
    time.sleep(0.0)
    for i in range(ML):
        L[i].undraw()

