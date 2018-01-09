# -*- coding: utf-8 -*-
import random #uvoz biblioteke random
spil = list() #globalna promenljiva
#funkcije:
def formirajSpil():
    znak = ["karo", "herc", "tref", "pik"]
    for i in range(2, 15):
        for j in znak:
            n = (str(i) + "_" + j)
            spil.append(n)

def izvuciKartu():
    r = random.randrange(0, len(spil))
    k = spil[r]
    del spil[r]
    return k

def vrednostKarte(k):
    broj = k.split("_")[0]
    if int(broj) < 12:
        vrkarte = int(broj)
    elif 11 < int(broj):
        vrkarte = 10
    return vrkarte

def vrednostA(vr):
    print("Dobio si A (11), a trenutna vrednost tvojih karata je " + str(vr) + ".")
    a = int(input("Da li zelis da se on racuna kao 1 ili kao 11? ('1'/'11'):"))
    while a != 1 and a != 11:
        a = int(input("Da li zelis da se on racuna kao 1 ili kao 11? ('1'/'11'):"))
    if a == 1:
        v = 1
    elif a == 11:
        v = 11
    return v

def novaKarta():
    nk = izvuciKartu()
    vnk = vrednostKarte(nk)
    return vnk

def blackJack():
    ime = input("Unesite svoje ime:")
    print("Zdravo, " + str(ime)+ ". Igramo igru Black Jack.")
    #formiranje spila karata
    formirajSpil()
    #izvlacenje karata
    k1 = izvuciKartu()
    #k1 = "11_tref"
    k2 = izvuciKartu()
    #pocetak igre
    print("Dobio si dve karte, to su: " + k1 + " i " +k2)
    #vrednost izvucenih karata
    v1 = vrednostKarte(k1)
    v2 = vrednostKarte(k2)
    #vrednost pocetnih karata u zavisnosti od izvucene kombinacije
    vr = 0
    if v1 != 11 and v2 != 11:
        vr = v1 + v2
    elif (v1 == 11 and v2 == 10) or (v1 == 10 and v2 == 11):
        vr = v1 + v2
        print("Bravo!!! Dobio si BlackJack jer je vrednost podeljenih karata " + str(vr) + "!")
        print("\nK R A J   I G R E")
        return
    elif v1 == 11 and v2 == 11:
        print("Dobio si A A! Obzirom da vrednost karata prelazi granicu, jedan A postaje 1.")
        v2 = 1
        vr = v1 + v2
    elif v1 == 11 or v2 == 11:
        vr = v1 + v2
        if v1 == 11:
            v1 = vrednostA(vr)
        elif v2 == 11:
            v2 = vrednostA(vr)
        vr = v1 + v2
    print("Trenutna vrednost tvojih karata je " + str(vr) + ".")
    a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne'):")
    while a != "da" and a != "ne":
        a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne'):")
    if a == "da":
        while a == "da":
            nk = izvuciKartu()
            vnk = vrednostKarte(nk)
            print("Dobio si " + str(nk) + ".")
            if vnk == 11:
                v = vrednostA(vr+vnk)
                vr += v
            else:
                vr += vnk
            if vr > 21:
                print("Izgubio siii... Vrednost karata je presla 21.")
                print("\nK R A J   I G R E")
                return
            print("Trenutna vrednost tvojih karata je " + str(vr) + ".")
            a = input("Da li zelis da izvuces jos jednu kartu? ('da'/'ne'):")
    elif a == "ne":
        print("Sledi deljenje karata dileru.")
    dk1 = izvuciKartu()
    dk2 = izvuciKartu()
    print("Diler je dobio karte " + str(dk1) + " i " + str(dk2) + ".")
    dv1 = vrednostKarte(dk1)
    dv2 = vrednostKarte(dk2)
    dvr = dv1 + dv2
    if (dv1 == 11 and dv2 == 10) or (dv1 == 10 and dv2 == 11):
        pass
    elif dv1 == 11 and dv2 == 11:
        dvr = 12
    elif dv1 == 11 or dv2 == 11:
        if dvr < 17 and dv1 == 11:
            dv1 = 1
        elif dvr < 17 and dv2 == 11:
            dv2 = 1
        dvr = dv1 + dv2
    print("Pocetna vrednost dilerovih karata je " + str(dvr) + ".")
    if dvr >= vr and dvr > 16:
        print("Diler je pobedio.")
        print("\nK R A J   I G R E")
        return
    while dvr < 16 or dvr < vr:
        dnk = izvuciKartu()
        dvnk = vrednostKarte(dnk)
        if dvr > 10 and dvnk == 11:
            dvnk = 1
        print("Diler je dobio " + str(dnk) + ".")
        dvr += dvnk
        print("Dilerova ruka je " + str(dvr) + ".")
        if dvr > 21:
            print("Dilerova ruka je presla 21, ti si pobednik!")
            print("\nK R A J   I G R E")
            return
        if dvr >= vr:
            print("Diler je pobedio.")
            print("\nK R A J   I G R E")
            return
    print("\nK R A J   I G R E")
blackJack()