#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py

def potega_it(x, n):

    i = 1
    wynik = 1
    while i <= n:
        wynik = wynik * x
        
        return wynik


# potęga _rek(a, n)= 1 dla a różnego od 0
# potęga _rek(a, n)= potega_rek(a, n - 1) * a dla n =  
def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n - 1) * a 
 
def main(args):
    x = float(input('Podaj podstawowe potegi: '))
    n = int(input('Podaj wykładnik potęgi: '))
    assert type(n) == int
    assert silnia_it(2,2) == 2
    assert silnia_it(3,2) == 9
    assert silnia_it(4,2) == 16
    assert silnia_it(5,2) == 25
    print('Wynik:')
    print (potega_it(x, n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
