# -*- coding: utf-8 -*-
Unos = raw_input("Unesi p ili d: ")
niz1 = [1, 5, 10]
niz2 = [3, 12, 20]
if Unos == "p":
    rezultat = [None]*(len(niz1)+len(niz2))
    rezultat[::2] = niz1
    rezultat[1::2] = niz2
    print rezultat
elif Unos == "d":
    rezultat = [None]*(len(niz1)+len(niz2))
    rezultat[::2] = niz2
    rezultat[1::2] = niz1
    print rezultat
