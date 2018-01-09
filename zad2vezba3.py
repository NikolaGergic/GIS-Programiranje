# -*- coding: utf-8 -*-
import math
class Tacka:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pomeri_X(self, x_pomeraj):
        self.x = float(self.x) + x_pomeraj
    def pomeri_Y(self, y_pomeraj):
        self.y = float(self.y) + y_pomeraj

    def ratojanje_do(self, tacka):
        rastojanje = math.sqrt((self.x-tacka.x)**2 + (self.y-tacka.y)**2)
        return rastojanje

class Duz:
    def __init__(self, p = 0, k = 0):
        self.p = p
        self.k = k
    def kreiranje_Duzi(self, xp,yp,xk,yk):
        p = Tacka(xp, yp)
        k = Tacka(xk, yk)
        d = Duz(p, k)
        return d

    def duzina_Duzi(self):
        return self.p.rastojanje_do(self.k)

    def str(self):
        print self.p.x, self.p.y, self.k.x, self.k.y,
    def __str__(self):
        return "Koordinata x pocetne tacke: {0:s}, Koordinata y pocetne tacke: {1:s}, Koordinata x krajnje tacke: {2:s}, Koordinata y krajnje tacke: {3:s}".format( str(self.p.x), str(self.p.y), str(self.k.x), str(self.k.y))

# Glavni program
xp = raw_input("Unesite X koordinatu pocetne tacke: ")
yp = raw_input("Unesite Y koordinatu pocetne tacke: ")
xk = raw_input("Unesite X koordinatu krajnje tacke: ")
yk = raw_input("Unesite Y koordinatu krajnje tacke: ")
pocetna = Tacka(xp,yp)
krajnja = Tacka(xk, yk)
a = Duz(pocetna, krajnja)
b = Duz(pocetna, krajnja)
c = b.kreiranje_Duzi(5,2,4,6)
print a.__str__()
print c.__str__()
dx = float(raw_input("Unesite dx: "))
dy = float(raw_input("Unesite dy: "))
krajnja.pomeri_X(dx)
krajnja.pomeri_Y(dy)
e = Duz(pocetna, krajnja)
print "Krajnja duz je: ", e.str()