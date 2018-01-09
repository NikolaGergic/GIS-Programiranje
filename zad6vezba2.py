# -*- coding: utf-8 -*-
import numpy as np
broj_tac = input("Unesite broj tacaka: ")
x = []
y = []
i = 0
while i < broj_tac:
    x.append(input("Unesi x koordinatu: "))
    y.append(input("Unesi y koordinatu: "))
    i = i + 1

step_polinoma = input("Unesi stepen polinoma: ")
koef = np.polyfit(x,y, step_polinoma)
fit = np.poly1d(koef)
print "Oblik polinoma je: ", fit
