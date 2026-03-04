#4 tehtava

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

#5 tehtava

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