#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ciag_rek.py
#  


def ciag_rek(n):
    if n == 1:
        return 2
    return ciag_rek(cieg_rek(n - 1) * n^2 + 1)
    
    
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
