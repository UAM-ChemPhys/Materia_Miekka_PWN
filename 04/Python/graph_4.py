from graphics import *
def rysujOkno(rozmiar_okna):
    oknoGraf = GraphWin('Random walk', rozmiar_okna, rozmiar_okna)
    oknoGraf.setCoords(0, 0, rozmiar_okna - 1, rozmiar_okna - 1)
    return oknoGraf
def rysuj(OknoGraf, rozmiar_okna, x, y, ML):
    asp = 5
    L=[0]
    for i in range(ML - 1):
        L.append(0)
    for i in range(ML - 1):
        x1 = int(x[i] * asp) + int(rozmiar_okna / 2)
        y1 = int(y[i] * asp) + int(rozmiar_okna / 2)
        x2 = int(x[i + 1] * asp) + int(rozmiar_okna / 2)
        y2 = int(y[i + 1] * asp) + int(rozmiar_okna / 2)
        L[i] = Line(Point(x1, y1), Point(x2, y2))    
        L[i].draw(OknoGraf)
    time.sleep(0.5)        
    for i in range(ML - 1):    
        L[i].undraw()


