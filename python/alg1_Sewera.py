#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alg1_Sewera.py  



def main(args):
    a = 0
    while a < 1 or a > 99:
        a = int(input("Podaj liczbę(1-99): "))
        #~for i in range(2, 101, 2):
            #~if a == i:
                #~print("Liczba parzysta")
                #~break
        #~if i == 100:
            #~print("Liczba nieparzyasta")
        i = 2
        while i < 100:
            if a == i:
                print("liczba parzysta")
                break
            i += 2
        if i == 100:
                print("Liczba nieparzysta")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
