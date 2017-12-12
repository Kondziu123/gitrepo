#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nww_v1(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    
    return a
         
def nwd_rek(a, b):
    if b == 0:
        return a 
    return nwd_rek(b, a % b)

def main(args):
    a = int(input('Podaj liczbe naturalną: '))
    b = int(input('Podaj liczbe naturalną: '))
    assert nww_v1(5,10) == 5
    assert nww_v1(20,100) == 20
    assert nww_v1(4,2) == 2
    print('NWD({:d}, {:d}) = {:d}'.format(a, b, nww_v1(a, b)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
