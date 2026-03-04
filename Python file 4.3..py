#Kertaustehtävät 4.3.

#1

nimi = input("Kerro nimesi: ")
if nimi == "Matti":
    print("Seuraava, kiitos!")

else :
    annokset = int(input("Montako keittoannosta? "))
    hinta = annokset * 5.90
    print("Kokonaishinta on", hinta)

    print("Seuraava, kiitos!")


#2

palkka = float(input("Kerro tuntipalkkasi:"))
tunnit = float(input("Montako tuntia olet tehnyt?"))
paiva = input("Mikä viikonpäivä?")

if paiva == "sunnuntai:":
    print("Paivapalkkasi on", palkka * tunnit * 2)
else:
    print("Paivapalkkasi on", palkka * tunnit)


#3

from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku:"))

    if luku < 0:
        print("Virheellinen numero.")
    elif luku > 0:
        print("Lukusi neliöjuuri on", sqrt(luku))
    else:
        print("Exiting...")
        break


#4

tarina = ""
edellinen = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan:")
    if sana == "Loppu" or sana == edellinen:
        break

    tarina += sana + " "
    edellinen = sana
    print(tarina)


#5

import math

while True:
    lasku = input("Valitse laskutoimitus. (Loppu lopettaa ohjelman)")

    if lasku == "Loppu":
        break

    luku1 = float(input("Anna ensimmmäinen luku:"))
    luku2 = float(input("Anna toinen luku:"))

    if lasku == "Yhteenlasku":
        print("Lukujesin yhteenlasku on", luku1 + luku2)
    elif lasku == "Vähennyslasku":
        print("Lukujesi vähennyslaskun tulos on", luku1 - luku2)
    elif lasku == "Kertolasku":
        print("Lukujesi kertolaskun tulos on", luku1 * luku2)
    elif lasku == "Jakolasku":
        print("Lukujesi jakolaskun tulos on", luku1 / luku2)







