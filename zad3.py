# -*- coding: utf-8 -*-


a1 = int(input('Unesite stepene prvog ugla: '))
b1 = int(input('Unesite minute prvog ugla: '))
c1 = int(input('Unesite sekunde prvog ugla: '))

a2 = int(input('Unesite stepene drugog ugla: '))
b2 = int(input('Unesite minute drugog ugla: '))
c2 = int(input('Unesite sekunde drugog ugla: '))

print ('Vrednost prvog ugla iznosi ') + str(a1) + '° ' + str(b1) + "' " + str(c1) + "''"
print ('Vrednost drugog ugla iznosi ') + str(a2) + '° ' + str(b2) + "' " + str(c2) + "''"
print('\n')

ugao1Dec = a1 + float(b1)/60 + float(c1)/3600
ugao2Dec = a2 + float(b2)/60 + float(c2)/3600


razlikaDec = round((ugao1Dec - ugao2Dec),4)

print ('Vrednost razlike uglova iznosi ') + str(razlikaDec)