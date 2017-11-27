# -*- coding: utf-8 -*-

a = int(input('Unesite prvi četvorocifreni broj: '))
b = int(input('Unesite drugi četvorocifreni broj: '))


suma = 0

while (b > 0):
    n = b % 10
    suma = suma + n
    b = b // 10

print('Suma cifara drugog broja je ') + str(suma)

cifre = []

while a> 0:
    cifre.append(a%10)
    a //= 10

par = cifre[1] + cifre[3]
nepar = cifre[0] + cifre[2]

razlika = par - nepar

print ('Razlika izmedju parnih i neparnih cifara prvog broja je ') + str(razlika)