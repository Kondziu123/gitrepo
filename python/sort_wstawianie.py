#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_wstawianie.py
#  
from math import floor

def sort_wstaw(lista):
    for i in range(1,len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:
            lista[k + 1] = lista[k]
            k = k - 1
        lista[k + 1] = el
    return lista


def szukaj_bin(l, p, lista, el):
    while l < p:
        srodek = floor((l + p) / 2)
        if el <= lista(srodek):
            p = srodek
        else:
            l = srodek + 1
    return l

def sort_wstaw_bin(lista):
    for i in range(1,len(lista)):
        el = lista[i]
        k = szukaj_bin(0, i, lista, el)
        lista = lista[:k] + [el] + lista[k:i] + lista[i + 1:]
        print(lista)
    return lista
        
        
def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    print(lista)
    print(sort_wstaw(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
