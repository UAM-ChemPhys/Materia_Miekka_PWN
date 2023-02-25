from graphics import *

def draw0(dim1, dim2):
    win = GraphWin('Signal', dim1, dim2)
    win.setCoords(0, 0, dim1 - 1, dim2 - 1)
    return win

def draw1(win, dim1, dim2, x1, x2, y1, y2, xmax, ymax):
    xg1 = round(dim1 * x1 / xmax)
    yg1 = dim2 - round(dim2 * (1 - y1 / ymax / 2))
    xg2 = round(dim1 * x2 / xmax)
    yg2 = dim2 - round(dim2 * (1 - y2 / ymax / 2))
    if (yg1 > 0) and (yg2 > 0):
        L = Line(Point(xg1, yg1), Point(xg2, yg2))
        L.draw(win)
