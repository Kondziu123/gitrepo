#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input('Ile liczb chce zgadywać'))
    maksliczb = int(input('Maksymalna losowana liczba:'))

    liczby = []

    for i in range(ileliczb):
        liczba = (random.randint(0, maksliczba))
        if liczby.count(liczba) == 0:
           liczby.append(liczba)

    print(liczby)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
