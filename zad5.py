# -*- coding: utf-8 -*-
a = int(input('Unesite prvi petocifreni broj: '))

maksimum = -1

for b in str(a):
    i = int(b)
    if i > maksimum:
        maksimum = i

print ('Najveća cifra u unetom broju je: ') + str(maksimum)