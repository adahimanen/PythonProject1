#1 tehtava

luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1


#2 tehtava

while True:
    tuumat = float(input("Anna tuumamäärä, negatiivinen luku lopettaa:"))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    senttimetrit = tuumat * 2.5
    print(f"{tuumat} tuumaa on {senttimetrit} cm")


#3 tehtava

luvut = []

while True:
    syöte = input("Anna luku (tyhjä lopettaa):")

    if syöte == "" :
        break

    luku = float(syöte)
    luvut.append(luku)

if len(luvut) > 0:
    print(f"Pienin luku: {main(luvut)}")
    print(f"Suurin luku: {max(luvut)}")

else:
    print("Lukuja ei syötetty.")

# 4 tehtava

import random

oikea_luku = random.randint(1, 10)
while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1-10: "))
        if arvaus > oikea_luku:
            print("Liian suuri arvaus")
        elif arvaus < oikea_luku:
            print("Liian pieni arvaus")
        else:
            print("Oikein")
            break

    except ValueError:
        print("Anna kelvollinen kokonaisluku")

# 5 tehtava

yritykset = 0
oikea_tunnus = "Python"
oikea_salasana = "Rules"

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break

    else:
        yritykset += 1
        if yritykset == 5:
            print("Pääsy evätty")
        else:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen. ")






