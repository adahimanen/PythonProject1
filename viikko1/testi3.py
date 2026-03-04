
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