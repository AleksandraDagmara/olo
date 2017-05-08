from pprint import pprint
with open ('starwars.txt', 'r') as file:
    c=file.readlines()
#pprint(c)
slownik={}
for zdanie in c:
    imie=zdanie.split(' has ')[0].split('. ')[1]
    pprint(imie)
    kolor_oczu=zdanie.split(' has ')[1].split('and is')[0]
    wzrost=zdanie.split(' has ')[1].split(' and is')[1].split('cm')[0].strip()
    #pprint(imie)
    #pprint(kolor_oczu)
    #pprint(wzrost)
    slownik[imie]={'kolor_oczu':kolor_oczu,'wzrost':wzrost}
#print(slownik)
#{'Lobo':('red',176)}
#wzrost_1=slownik.values()
    #slownik_1[imie]=wzrost
#for klucz, wartosc in slownik.items():
    #print (klucz, wartosc)

for klucz in slownik:
    print (klucz, slownik[klucz]['wzrost'])


