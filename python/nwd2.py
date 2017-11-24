#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nwd_v1(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    
    return a
    
    
def nwd_v2(a,b):
    while a > 0:
        a = a % b
        b = b - a
    return b
    
            
def main(args):
    a = int(input('Podaj liczbe naturalną: '))
    b = int(input('Podaj liczbe naturalną: '))
    assert nwd_v2(5,10) == 5
    assert nwd_v2(20,100) == 20
    assert nwd_v2(4,2) == 2
    print('NWD({:d}, {:d}) = {:d}'.format(a, b, nwd_v2(a, b)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
