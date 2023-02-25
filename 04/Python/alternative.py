
# *****************************************************
        for probuj in range(100):
            if warunki_SAW(x, y, x2, y2, Liczba-1):
                dx, dy = przesuniecie[random.randint(0, 3)]
                x2 = x[Liczba - 1] + skok_x
                y2 = y[Liczba - 1] + skok_y
        if warunki_SAW(x, y, x2, y2, Liczba-1):
           break
        else:
           x.append(x[Liczba-1] + skok_x)
           y.append(y[Liczba-1] + skok_y)
           OdlKwadr[Liczba]+=x[Liczba]**2+y[Liczba]**2
           IleLancuchow[Liczba] += 1
# *****************************************************

