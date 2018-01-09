# -*- coding: utf-8 -*-
import math
class Sfera:
    promenljiva = 0
    def __init__(self,r = 1,x = 0,y = 0,z = 0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
        Sfera.promenljiva += 1

    @staticmethod
    def Statisticka():
         return Sfera.promenljiva
    def zapLopte(self):
         v = (self.r)
         return (4 / 3) * v ** 3 * math.pi

# Glavni program Sfera

print Sfera.Statisticka()
sfera = Sfera(0, 0, 0, 4.0)
globus = Sfera(1.0, 1.0, 1.0, 12)
bilijarska_lopta = Sfera(10.0, 10.0, 10.0, 10.0)
jedinicna_sfera = Sfera()
print Sfera.Statisticka()
print "Zapremina sfere je", sfera.zapLopte()
print "Zapremina globusa je", globus.zapLopte()
print "Zapremina bilijarske_lopte je", bilijarska_lopta.zapLopte()
print "Zapremina jedinicne_sfere je", jedinicna_sfera.zapLopte()



