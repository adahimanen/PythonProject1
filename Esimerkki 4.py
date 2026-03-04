hinta = 5
rahaa_annettu = 0

while rahaa_annettu < hinta:
    rahaa_annettu += 1
    print("Rahaa annettu:", rahaa_annettu)
print("Kahvi maksettu")



while True:
    rahaa_annettu += 1
    print("Rahaa annettu:", rahaa_annettu)

    if rahaa_annettu == hinta:
        break

print("Kahvi maksettu")

käsky = input("Annetaanko lisää rahaa ('ei' )

while kasky != "ei":
    print("annettu kolikko lisää.")
    käsky = input("Annetaanko lisää rahaa?")

print("Ohjelma päättyy.")



summa = 0

while True:
    numero = int(input("Anna luku jonka haluat lisätä, -1 lopettaa: "))
    if numero == -1:
        break
    elif numero >= 10:
        continue
    summa += numero
print("Summa on:", summa)



käsky = input("Annetaanko lisää kolikoita?")

while käsky != "ei":
    if käsky == "ryöstö":
        print("Kolikot ryöstetty")
        break
    print("Annetaan kolikko")
    käsky = input("Annetaanko lisää kolikoita?")
else:
    print("Hyvästi!")

print("Ohjelma loppuu")





