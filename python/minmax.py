#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  

import random

def losuj(ileliczb, maksliczb):
    liczby = []
    ile = 0
    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1

    print(liczby)
    return liczby


def minimum(lista):
    min = lista[0]
    for i, el in enumerate(lista):
        if el < min:
            min = el

    return min

def maksimum(lista):
    """Wyszukiwanie maksimum"""
    max = lista[0]
    for i, el in enumerate(lista):
        if el > max:
            max = el

    return max

def main(args):
    lista = losuj(10, 50)
    assert minimum([7, 5 , 2, 1, 7]) == 1
    assert maksimum([7, 5 , 2, 1, 7]) == 7
    print("Min: ", minimum(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))