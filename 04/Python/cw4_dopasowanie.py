import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.offsetbox import AnchoredText

def rysuj():
    # Odczyt danych
    nazwa_pliku_z_danymi='wyniki.txt'
    plik_dane=open(nazwa_pliku_z_danymi,"r")
    linie=plik_dane.readlines()
    liczba_krokow=[float(x.split()[0]) for x in linie]
    odl_kwadr=[float(x.split()[1]) for x in linie]
    liczba_konformacji=[float(x.split()[2] ) for x in linie]
    plik_dane.close()

    # Zlogarytmowanie
    log_liczba_krokow = np.log(liczba_krokow)
    log_odl_kwadr = np.log(odl_kwadr)

    # ------------------------
    # Analiza wszystkich punktow
    # ------------------------

    # Dopasowanie linii prostej
    nachylenie, wyraz_wolny, r_value, p_value, std_err = stats.linregress(log_liczba_krokow, log_odl_kwadr)
    print("nachylenie: %f    wyraz wolny: %f" % (nachylenie, wyraz_wolny))

    # Przygotowanie wykresow
    wykres1, (ax1, ax2) = plt.subplots(2,1, figsize=(8, 6), sharex = True)
    ax1.set_title('Analiza wszystkich punktow')
    ax1.plot(log_liczba_krokow, log_odl_kwadr, '.', label='oryginalne dane')
    ax1.plot(log_liczba_krokow, wyraz_wolny + nachylenie*log_liczba_krokow, 'r', label='linia dopasowania')
    ax1.set_ylabel('log(h)')
    ax1.legend(loc = 'lower right')
    rownanie_prostej = 'y = ' + str('%1.4f'%nachylenie) + 'x + ' + str('%1.4f'%wyraz_wolny)
    ax1.text(0., np.max(log_odl_kwadr)*0.9, rownanie_prostej, bbox=dict(facecolor='none', edgecolor='black', boxstyle = 'round'), fontsize = 12, color = 'red')

    ax2.plot(log_liczba_krokow, liczba_konformacji)
    ax2.set_ylabel('liczba udanych symulacji')
    ax2.set_xlabel('log(N)')
    plt.pause(0.001)
    input("Wcisnij [enter] aby kontynuowac")

    # ------------------------
    # Analiza wybranych punktow
    # ------------------------

    # Gorna granica
    gorna_granica = float(input('gorna granica = '))
    i = 0
    for m in log_liczba_krokow:
        if m < gorna_granica:
            i += 1

    # Dopasowanie linii prostej dla wybranych punktow
    nachylenie, wyraz_wolny, r_value, p_value, std_err = stats.linregress(log_liczba_krokow[:i], log_odl_kwadr[:i])
    print("nachylenie: %f    rzedna poczatkowa: %f" % (nachylenie, wyraz_wolny))

    # Przygotowanie wykresow dla wybranych punktow
    wykres2, (ax1, ax2) = plt.subplots(2,1, figsize=(8, 6), sharex = True)
    ax1.set_title(f'Analiza dla punktów dla log(N) $\leq$  {gorna_granica}' )
    ax1.plot(log_liczba_krokow[:i], log_odl_kwadr[:i], '.', label='oryginalne dane')
    ax1.plot(log_liczba_krokow[:i], wyraz_wolny + nachylenie * log_liczba_krokow[:i], 'r', label='linia dopasowania')
    ax1.set_ylabel('log(h)')
    ax1.legend(loc = 'lower right')
    rownanie_prostej = 'y = ' + str('%1.4f' % nachylenie) + 'x + ' + str('%1.4f' % wyraz_wolny)
    ax1.text(0., np.max(log_odl_kwadr[:i]) * 0.9, rownanie_prostej,
             bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'), fontsize=12, color='red')

    ax2.plot(log_liczba_krokow[:i], liczba_konformacji[:i])
    ax2.set_ylabel('liczba udanych symulacji')
    ax2.set_xlabel('log(N)')

    plt.show()

# Wywołanie glownej funkcji programu
rysuj()
