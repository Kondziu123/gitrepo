#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_bubll.py 
#  
import random
 
def losuj(rozmiar, od, do): 
    tab=[]                  
    while rozmiar>0: 
        tab.append(random.randint(od,do))
        rozmiar-=1 
    return tab
 
    for i in range(len(tab)):
        j=len(tab)-1
    while j>i:   
        if tab[j]<tab[j-1]: 
            tmp=tab[j]
            tab[j]=tab[j-1]
            tab[j-1]=tmp
            j-=1
    return tab
 
def main(args):
tab=losuj(10, 1,10)
print "przed: "+str(tab)
tab=sort(tab)
print "   po: "+str(tab)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
