from graphics import *

def draw0(dim):
    win = GraphWin('Random walk', dim, dim)
    win.setCoords(0, 0, dim - 1, dim - 1)
    return win
    
def draw1(win, dim, edge, C, ML):

    p1=0
    p2=1
    p3=2
    asp = 10
    E=edge/2
    shift=0.5
    L=[0]
    for i in range(ML):
        L.append(0)
    for i in range(ML):
        x1 = int((C[i,p1]-E+(C[i,p3]-E)*shift)*asp+dim/2)
        y1 = int((C[i,p2]-E+(C[i,p3]-E)*shift)*asp+dim/2)
        x2 = int((C[i+1,p1]-E+(C[i+1,p3]-E)*shift)*asp+dim/2)
        y2 = int((C[i+1,p2]-E+(C[i+1,p3]-E)*shift)*asp+dim/2)
        L[i] = Line(Point(x1, y1), Point(x2, y2))
        L[i].draw(win)
    time.sleep(0.1)        
    for i in range(ML):    
        L[i].undraw()
           
 