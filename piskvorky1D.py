import random  # (příp. import jiných věcí, které budou potřeba)

def tah(pole, cislo_policka, symbol):
    """Vrátí pole s daným symbolem umístěným na danou pozici"""
    pole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return pole

def tah_hrace(pole):
    """Zeptá se hráče kam chce hrát a vrátí pole se zaznamenaným tahem"""
    while True:
        tah_hrace = int(input('Kam chceš hrát? '))
        if tah_hrace >= 0 and tah_hrace < 20:
            if pole[tah_hrace] == '-':
                return tah_hrace
            else:
                print('Toto pole je již obsazené.')
        else:
            print('Pole musí být v rozmezí od 0 do 19!')

def ukonceni_hry(pole):
    if 'xxx' in pole or 'ooo' in pole:
        if 'xxx' in pole:
            cislo_hrace = 1
        else:
            cislo_hrace = 2
        konec = f'Gratuluji, vyhrál hráč číslo {cislo_hrace}.'
    elif '-' not in pole:
        konec = 'Je to remíza. Nejsou možné žádné další tahy.'
    else:
        konec = ''
    return konec

def piskvorky1d():
    """Spustí hru. Vytvoří hrací pole a střídavě volá tah_hrace a tah_pocitace dokud někdo nevyhraje"""
    pole = '-' * 20
    print('Hrací pole:', pole)
    while ukonceni_hry(pole) == '':
        for i in range(2):
            j = i + 1
            if j == 1:
                znak = 'x'
            else:
                znak = 'o'
            print('Hráč číslo', j, ' je na tahu.', end=' ')
            pole = tah(pole, tah_hrace(pole), znak)
            print(pole)
            konec = ukonceni_hry(pole)
            if konec != '':
                print(konec)
                break

# Puštění hry!
piskvorky1d()