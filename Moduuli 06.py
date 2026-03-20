#1tehtava

import random

# Parametriton funktio, joka palauttaa nopan silmäluvun 1-6
def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma
while True:
    tulos = heita_noppaa()
    print("Heitto:", tulos)

    if tulos == 6:
        break



#2tehtava

import random

# Funktio saa parametrina tahkojen määrän
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# Paaohjelma
tahkot = int(input("Anna nopan tahkojen määrä: "))

while True:
    tulos = heita_noppaa(tahkot)
    print("Heitto:", tulos)

    if tulos == tahkot:
        break



#3tehtava

# Funktio muuntaa gallonat litroiksi

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

# Pääohjelma

while True:
    maara = float(input("Anna bensiinin määrä galloonina (negatiivinen lopettaa):"))

    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print("Määrä litroina:", litrat)




#4tehtava

# Funktio joka laskee listan lukujen summan
def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku

    return summa

# Paaohjelma (testi)

luvut = [1, 2, 3, 4, 5]

tulos = laske_summa(luvut)
print("Listan summa on:", tulos)




#tehtava 5

# Funktio, joka poistaa parittomat luvut

def poista_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista

# Paaohjelma (testi)

luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]

karsittu = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista (vain parilliset):", karsittu)




#tehtava 6

import math

# Funktio laskee pizzan yksikköhinnan (€/m^2)

def yksikkohinta(halkaisija_cm, hinta_euroina):
    sade_m = (halkaisija_cm / 2) / 100 # muutetaan sade metreiksi
    pinta_ala = math.pi * sade_m ** 2 # ympyran pinta-ala
    return hinta_euroina / pinta_ala

# Paaohjelma

# Pizza 1
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

# Pizza 2
halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

# yksikköhinnat
yks1 = yksikkohinta(halkaisija1, hinta1)
yks2 = yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yks1:.2f} €/m^2 ")
print(f"Toisen pizzan yksikköhinta: {yks2:.2f} €/m^2 ")

# kumpi parempi
if yks1 < yks2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle. ")

elif yks2 <yks1:
    print("Toinen pizza antaa paremman vastineen rahalle. ")

else:
    print("Pizzat ovat yhtä edullisia. ")