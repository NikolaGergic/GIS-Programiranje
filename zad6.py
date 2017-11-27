# -*- coding: utf-8 -*-
a = unicode(raw_input('Unesite pet karaktera: '))

b = 0
for c in a:
    if c.isdigit():
        b += 1
print ('Broj cifara u unetim karakterima je: ') +  str(b)
