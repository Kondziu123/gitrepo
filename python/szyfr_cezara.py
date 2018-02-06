#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szyfr_cezara.py


def szyfruj_cezar(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ""
    for znak in tekst:
        znak = znak.upper()
        ascii = ord(znak) + klucz
        if ascii > 90:
            ascii -= 26
        szyfrogram += chr(ascii)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    pass

# obsłużyć spacje
# obsłużyc małe i duże litery


def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Klucz: "))
    
    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
