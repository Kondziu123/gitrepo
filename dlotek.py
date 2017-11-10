#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def pobierz_typy(ileliczb):
    typy = set()
    # for i in range(ileliczb):
    ile = 0
    while ile < ileliczb:
        typ = int(input('Podaj typ: '))
        if typ not in typy:
            typy.add(typ)
            ile += 1

    # print(typy)
    return typy


def main(args):
    ileliczb = int(input('Ile liczb chce zgadywać'))
    maksliczb = int(input('Maksymalna losowana liczba:'))

    while ileliczb > maksliczb or ileliczb < 1:
        ileliczb = int(input('Ile iczb chcesz zgadnąć z %s liczb' % maksliczb))

    liczby = losuj(ileliczb, maksliczb)
    typy = pobierz_typy(ileliczb)

    trafione = set(liczby) & typy
    print('Trafiłeś', len(trafione), 'liczb')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
