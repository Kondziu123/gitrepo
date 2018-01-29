#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konwersje.py

def konwersja1(liczba10, podstawa):
    """
    Funkcja zamienia liczbę dziesietną na system o podanej podstawie
    """
    liczba = []
    while liczba10 != 0:
        reszta = liczba10 % podstawa
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczbaa10 = int(liczba10 / podstawa)
    
    liczba.reverse()
    return "".join(liczba)
            
            
def dec2other():
    """
    Funkcja pobiera liczbe i podstawe od użytkownika
    """
    liczba = int(input("Podaj liczbę: "))
    podstawa = int(input("Podaj podstawe: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawe: "))
    print("Wynik konwersji: {}(10) = {}({})".format(
        liczba, konwersja1(liczba, podstawa), podstawa))


def main(args):
    print("Zamiana liczby dziesiettnej o podanej podstawie"
        "<2;16> lub odwrotnie.")
    dec2other()
    other2dec()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
