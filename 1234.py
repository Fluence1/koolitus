from math import *

#print("Hello world!")
#print("meow \nwoof")
#print("yikes", end=" ")
#print("oof")
#print(7)
#print(5+5)
#pindala=20.34666
#print(pindala)
#print(pindala, "on pindala")
#kala=30
#print(pindala+kala)

#kokku=pindala*kala
#print(kokku)
#print("Pindala on %0.2f." % (pindala))

#kasutaja=input("Mis on su nimi? - ")
#print(kasutaja)

#arvEsimene= int(input("Esimene arv? - "))
#arvTeine= int(input("Teine arv? - "))

#print(arvEsimene + arvTeine)

#meieEsimene= ["politsei","tuletõrje","kiirabi"]
#print(meieEsimene[1])

#meieTeine= ["hommik","lõuna","õhtu"]
#print(meieEsimene + meieTeine)

#kasutaja=int(input("Mis on ruudu külje pikkus? - "))
#print(kasutaja)
#pindala=(kasutaja*kasutaja)
#print(pindala)

#alus=int(input("Mis on kolmnurga alus? - "))
#print(kasutaja)
#kõrgus=int(input("Mis on kolmnurga kõrgus? - "))
#print(kasutaja)
#pindala=(alus*kõrgus/2)
#print(pindala)

#print(abs(-3)) #absoluutväärtus
#print(round(2.6375, 2)) #ümardamine
#print(round(2.675))
#print(5**3)  #astendamine (5 astmes 3)
#print(5//3) #mitu korda täisarvuliselt üks arv jagnueb teisega

#tester = False
#topelt = True

#if 5+1==6:
    #print(topelt)
#if 5-4==7:
    #print(tester)

#kasutaja=input("Ütle mingi värv - ")
#print(kasutaja)
#sinine = 1
#punane = 2
#must = 3
#if kasutaja == "sinine":
    #print(1)
#if kasutaja == "punane":
    #print(2)
#if kasutaja == "must":
    #print(3)

#Kasutaja sisestab mingi nime.
#nimi= "tester"
#print(len(nimi))
#if len(nimi)>8:
    #print("Liiga pikk")
#Teha nii, et küsiks kasutajalt nime, ei tohi olla pikem kui 20 tähte ja ei tohi olla lühem kui 8 tähte.
#nimi=input("Sisesta nimi - ")

#if len(nimi)>20:
    #print("Liiga pikk")
#if len(nimi)<8:
    #print("Liiga lühike")    #kui see on true siis elif'i ei tee ja kui see on false siis teeb
#elif len(nimi)>3:
    #print("Tõene!")
#else:
    #print("Nojah")      #kui ta ei saa eelnevaid tehtud siis teeb else'i, kui ta saab eelnevaid tehtud siis ta else'i ei tee

#if 2==3 and 2==2:
    #print("test1")
#elif 2==4:
    #print("test2")
#else:
    #print("Nojah")

#if 3>2: print("shorthand")           #kui if'iga on ainult üks tegevus siis shorthand, kui rohkem siis pole mõtet

#if 3==4 or 4==4:
    #print("on olemas")

#if 4==4:
    #if 5==4:
       #print("on olemas nested if")

#kasutaja sisestab arvu, meie vastame talle, kas tegemist on paarisarvu või paaritu arvuga
#arv=int(input("Sisesta arv - "))
#if arv%2==0:
    #print("Paaris arv")
#else:
    #print("Paaritu arv")

#Liigaasta
#Kirjuta programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta.
#aasta on liigaasta, kui tema number jaguneb neljaga, välja arvatud need aastad mille number jagub sajaga, kuid ei jagu neljasajaga)
aasta=int(input("Kirjuta aasta - "))
if aasta%100==0:
    if aasta%400!=0:
        print("Lihtaasta")
    else:
        if aasta%4==0:
            print("Liigaasta")
        else:
            print("Lihtaasta")
else:
    if aasta%4==0:
        print("Liigaasta")
    else:
        print("Lihtaasta")




