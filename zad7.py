# -*- coding: utf-8 -*-
import math

"""Do zaključka da se tačka nalazi u trouglu se došlo na osnovu znaja teorije 
da se tačka sigurno nalazi u trouglu ukoliko je zbir uglova koje ona gradi sa temenima
 trougla jednak 360 stepeni i ako nijedan od tih uglova nije veći od 180 stepeni."""

x1 = int(input('Unesite x koordinatu tačke A:  '))
y1 = int(input('Unesite y koordinatu tačke A:  '))
x2 = int(input('Unesite x koordinatu tačke B:  '))
y2 = int(input('Unesite y koordinatu tačke B:  '))
x3 = int(input('Unesite x koordinatu tačke C:  '))
y3 = int(input('Unesite y koordinatu tačke C:  '))
x4 = int(input('Unesite x koordinatu tačke M:  '))
y4 = int(input('Unesite y koordinatu tačke M:  '))
print ('\n')

print ('A (') + str(x1) + (',') + str(y1) + (')')
print ('B (') + str(x2) + (',') + str(y2) + (')')
print ('C (') + str(x3) + (',') + str(y3) + (')')
print ('M (') + str(x4) + (',') + str(y4) + (')')

duzAB = math.sqrt((x1-x2)**2 + (y1-y2)**2)
duzAC = math.sqrt((x1-x3)**2 + (y1-y3)**2)
duzBC = math.sqrt((x2-x3)**2 + (y2-y3)**2)
duzAM = math.sqrt((x1-x4)**2 + (y1-y4)**2)
duzBM = math.sqrt((x2-x4)**2 + (y2-y4)**2)
duzCM = math.sqrt((x3-x4)**2 + (y3-y4)**2)

print ('\n')

ugaoAMB = math.acos((duzAM**2 + duzBM**2 - duzAB**2)/(2*duzBM*duzAM))
ugaoAMC = math.acos((duzAM**2 + duzCM**2 - duzAC**2)/(2*duzCM*duzAM))
ugaoBMC = math.acos((duzBM**2 + duzCM**2 - duzBC**2)/(2*duzCM*duzBM))


if (math.degrees(ugaoAMB) + math.degrees(ugaoAMC) + math.degrees(ugaoBMC)) == 360 and ugaoAMB <= 180 and ugaoAMC <= 180 and ugaoBMC <= 180:
    print ('Tacka M se nalazi u trouglu ABC')
else:
    print('Tacka M se ne nalazi u trouglu ABC')
