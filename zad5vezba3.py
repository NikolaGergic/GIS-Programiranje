# -*- coding: utf-8 -*-
from datetime import datetime
class Osoba:
    def __init__(self, ime, prezime, datum_rodj, adresa):
        self.ime = ime
        self.prezime = prezime
        self.datum_rodj = datum_rodj
        self.adresa_ = adresa
    def postavi_Ime(self, ime):
        self.ime = ime
    def postavi_Prezime(self, prezime):
        self.prezime = prezime
    def postavi_datum_rodj(self, datum_rodj):
        self.datum_rodj = datum_rodj
    def postavi_adresa(self, adresa):
        self.adresa = adresa
    def info(self):
        print "Ime:{0:s}, Prezime:{1:s}, Datum rodjenja:{2:s}, Adresa:{3:s}".format(str(self.ime), str(self.prezime), str(self.datum_rodj), str(self.adresa))
class Djak(Osoba):
    def __init__(self, ime, prezime, datum_rodj, adresa, skola = "Vuk Karadzic" , odeljenje = "VIII-4", god_upisa = "1999"):
        Osoba.__init__(self, ime, prezime, datum_rodj, adresa)
        self.skola = skola
        self.odeljenje = odeljenje
        self.god_upisa = god_upisa
    def razredDjaka(self):
        d = str(self.odeljenje)
        e = d.split("-")
        return e[0]
    def obnavljanje(self):
        uk_god = 8 #ukupno godina skolovanja
        god_upisa = self.god_upisa
        studiranje = 2017 - int(god_upisa)
        if studiranje <= uk_god:
            print "Ucenik nije obnovio godinu."
        else:
            print "Ucenik je obnovio godinu."



a = Djak("Nikola", "Gergic", "28 Januar", "Vojvode Misica", "Vuk Karadzic", "VI-2", "1980")
print a.razredDjaka()
print a.obnavljanje()

class Zaposlen(Osoba):
    def __init__(self, ime, prezime, datum_rodj, adresa, kompanija = "Delta", departman = "Marketing", dat_zakljucenja = "01.02.2016.", dat_prekida = "01.01.2016."):
        Osoba.__init__(self, ime, prezime, datum_rodj, adresa)
        self.kompanija = kompanija
        self.departman = departman
        self.dat_zakljucenja = dat_zakljucenja
        self.dat_prekida = dat_prekida
    def dajRadniStaz(self):
        vreme = datetime.now()
        god = vreme.year
        mes = vreme.month
        dat_zak = self.dat_zakljucenja
        dat_zak1 = dat_zak.split(".")
        mes1 = int(dat_zak1[1])
        god1 = int(dat_zak1[2])
        mesec = (god-god1)*12 + abs(mes-mes1)
        print "Radni staz u mesecima je: " ,mesec

zap = Zaposlen("Slavoljub", "Srnic", "29.01.1982.", "Rajka Mitica")
print zap.dajRadniStaz()

# Glavni Program

#Djak

a1 = raw_input("Unesite ime: ")
a2 = raw_input("Unesite prezime: ")
a3 = raw_input("Unesite datum rodjenja: ")
a4 = raw_input("Unesite adresu: ")
a5 = raw_input("Unesite skolu: ")
a6 = raw_input("Unesite odeljenje: ")
a7 = raw_input("Unesite godinu upisa: ")

GERG = Djak(a1, a2, a3, a4, a5, a6, a7)
print "Razred djaka je: ", GERG.razredDjaka()
print GERG.obnavljanje()

#Zaposleni

b1 = raw_input("Unesite ime: ")
b2 = raw_input("Unesite prezime: ")
b3 = raw_input("Unesite datum rodjenja: ")
b4 = raw_input("Unesite adresu: ")
b5 = raw_input("Unesite ime kompanije: ")
b6 = raw_input("Unesite ime departmana: ")
b7 = raw_input("Unesite datum zakljucenja: ")
b8 = raw_input("Unesite datum prekida: ")

NIKO = Zaposlen(b1, b2, b3, b4, b5, b6, b7, b8)
print NIKO.dajRadniStaz()
