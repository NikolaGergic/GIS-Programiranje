# -*- coding: utf-8 -*-
class Inzenjer:
    def __init__(self, ime, prezime, mat_br, licenca):
        self.ime = ime
        self.prezime = prezime
        self.mat_br = mat_br
        self.licenca = licenca
    def daj_ime(self):
        return self.ime
    def daj_prezime(self):
        return self.prezime
    def daj_mat_br(self):
        return self.mat_br
    def daj_licencu(self):
        return self.licenca
    def postavi_ime(self, ime):
        self.ime = ime
    def postavi_prezime(self, prezime):
        self.prezime = prezime
    def postavi_mat_br(self, mat_br):
        self.mat_br = mat_br
    def postavi_licencu(self, licenca):
        self.licenca = licenca

    def info(self):
        print "Ime: {0:s}, Prezime: {1:s}, Maticni broj: {2:s}, Licenca: {3:s}".format(str(self.ime),str(self.prezime),str(self.mat_br),str(self.licenca))
a = Inzenjer("Nikola", "Gergic", "1412", "geodetska")
a.info()



class GeodetskiInzenjer(Inzenjer):
    def __init__(self, ime, prezime, mat_br, licenca, br_staz):
        Inzenjer.__init__(self, ime, prezime, mat_br, licenca)
        self.br_staz = br_staz
    def daj_br_staz(self):
        return self.br_staz
    def postavi_br_staz(self, br_staz):
        self.br_staz = br_staz
    def info_g(self):
        print "Ime: {0:s}, Prezime: {1:s}, Maticni broj: {2:s}, Licenca: {3:s}, Broj staza: {4:s}".format(str(self.ime), str(self.prezime),str(self.mat_br), str(self.licenca), str(self.br_staz))

    def ispis_Lic(self):
        c = self.daj_licencu()
        if c == None:
            print "Geodetski inzenjer nema licencu."
        else:
            print "Geodetski inzenjer ima licencu."

b = GeodetskiInzenjer("Nikola", "Gergic", "1412", None, "15")
b.ispis_Lic()

class ElektrotehnickiInzenjer(Inzenjer):
    def __init__(self, ime, prezime, mat_br, licenca, br_proj):
        Inzenjer.__init__(self, ime, prezime, mat_br, licenca)
        self.br_proj = br_proj
    def daj_br_proj(self):
        return self.br_proj
    def postavi_br_proj(self, br_proj):
        self.br_proj = br_proj
    def info_e(self):
        print "Ime: {0:s}, Prezime: {1:s}, Maticni broj: {2:s}, Licenca: {3:s}, Broj projekata: {4:s}".format(str(self.ime), str(self.prezime),str(self.mat_br), str(self.licenca), str(self.br_proj))
    def ispis_Lic_e(self):
        v = self.daj_licencu()
        if v == None:
            print "Elektrotehnicki inzenjer nema licencu."
        else:
            print "Elektrotehnicki inzenjer ima licencu."
r = ElektrotehnickiInzenjer("Nikola", "Gergic", "1412", "WG-196", "7")
r.ispis_Lic_e()


