#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie.py
#  


def main(args):
    
    osoba = input("Jak sie nazywasz? ")
    print("witaj", osoba)
    
    dzialanie = input("dzialanie?")
    
    if dzialanie == "+":
        print(a + b)
    elif dzialanie == "-":
        print(a - b)
    
    return 0
    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
