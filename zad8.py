from random import randint

ime = str(raw_input('Unesi ime:'))
broj = (randint(0, 100))
print (broj)
unos = int(input('Unesite broj:'))

while unos != broj:
    unos = int(input('Promasili ste, pokusajte ponovo:'))

print ('Cestitamo! Trazeni broj je ') + str(unos)

