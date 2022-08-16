from turtle import forward, left, exitonclick, pendown, penup
import math

def vypocti_uhlopricku(vc, c):
    """Vypočítá délku úhlopříčky dle vzorečku z trojúhelníku a = sqrt (vc**2 + (c/2)**2)"""
    uhlopricka = math.sqrt((vc ** 2) + ((c / 2) ** 2))
    return uhlopricka

def vypocti_uhel(c, a):
    """Vypočítá úhel z trojúhelníku dle vzorce cosA = c/(2*a)"""
    uhel = c / (2 * a)
    uhel = math.asin(uhel)
    uhel = math.degrees(uhel)
    return uhel

def nakresli_domecek():
    """Nakreslí domeček dle dvou parametrů"""
    sirka = int(input('Zadej šířku domečku (1-200): '))
    vyska = int(input('Zadej výšku domečku (1-400): '))
    strecha = vyska / 3
    vyska = vyska - (vyska / 3)

    # posun doleva, aby byl domeček na středu
    penup()
    left(180)
    forward(sirka * 1.5)
    left(90)
    forward((vyska + strecha) / 2)
    left(90)
    pendown()

    # nakreslení základu
    forward(sirka)
    for i in range(4):
        if i == 0 or i % 2 == 0:
            strana = sirka
        else:
            strana = vyska
        forward(strana)
        left(90)

    # nakreslení úhlopříčky
    strana = vypocti_uhlopricku(sirka / 2, vyska)
    uhel = vypocti_uhel(vyska, strana)
    left(uhel)
    forward(strana * 2)  
    left(90 - uhel)

    # nakreslení střechy
    strana_strechy = vypocti_uhlopricku(strecha, sirka)
    uhel_strechy = vypocti_uhel(sirka, strana_strechy)
    left(uhel_strechy)
    forward(strana_strechy)
    left(180 - (2 * uhel_strechy))
    forward(strana_strechy)
    left(uhel_strechy)

    # nakreslení druhé úhlopříčky
    left(90 - uhel)
    forward(strana * 2)
    left(uhel)
    forward(sirka)

    exitonclick() 

nakresli_domecek()