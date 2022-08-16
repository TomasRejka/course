from random import choice

def volba_hrace():
    while True:
        hrac = input('Zvol kámen, nůžky nebo papír (nebo konec). Co zvolíš? ')
        if hrac == 'kámen' or hrac == 'nůžky' or hrac == 'papír' or hrac == 'konec':
            return hrac
        else:
            print('Zvolil jsi neplatnou volbu, zvol prosím znovu.')

def volba_pocitace():
    moznosti = ['kámen', 'nůžky', 'papír']
    pocitac = choice(moznosti)
    return pocitac

def spust_hru(skore_hrace, skore_pocitace):
    while True:
        print()
        hrac = volba_hrace()
        if hrac == 'konec':
            break
        pocitac = volba_pocitace()

        print('Zvolil jsi', hrac.upper() + ', počítač zvolil', pocitac.upper() + '.')

        # porovnání a přiřazení hodnoty první značí výhru a druhá zobrazenou hlášku
        if hrac == pocitac:
            vysledek = 'R0'
        elif hrac == 'kámen':
            if pocitac == 'nůžky':
                vysledek = '11'
            else:
                vysledek = '02'
        elif hrac == 'nůžky':
            if pocitac == 'papír':
                vysledek = '13'
            else:
                vysledek = '01'
        else:
            if pocitac == 'kámen':
                vysledek = '12'
            else:
                vysledek = '03'

        # Výpis výsledku
        if vysledek[0] == 'R':
            vyhra = f'Remíza, oba máte {hrac}.'
        if vysledek[0] == '1':
            skore_hrace = skore_hrace + 1
            vyhra = 'Gratuluji! Vyhrál jsi.'
        elif vysledek[0] == '0':
            skore_pocitace = skore_pocitace + 1
            vyhra = 'Bohužel jsi prohrál.'
        hlaska = int(vysledek[1])       

        if hlaska == 0:
            hlaska = ''
        elif hlaska == 1:
            hlaska = 'Kámen tupí nůžky.'
        elif hlaska == 2:
            hlaska = 'Papír balí kámen.'
        else:
            hlaska = 'Nůžky stříhají papír.'

        print(f'{vyhra} {hlaska} Skóre je', str(skore_hrace), ':', str(skore_pocitace) + '.')            
    
spust_hru(0, 0)