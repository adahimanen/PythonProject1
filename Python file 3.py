#1 tehtava

pituus=float(input("Kuinka pitkä kuha on?"))
if pituus<37:
    print("Laske kuha takaisin järveen.")
    print("Kuhan pitää olla",37 - pituus, " cm pidempi! ")

#2 tehtava

hyttiluokka=input("Mika on hyttiluokkasi?")
if hyttiluokka=="A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka=="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka=="C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka=="LUX":
    print("LUX on parvekkeellinen hytti yläkannella")

#3 tehtava

sukupuoli = input("Mikä on sinun biologinen sukupuoli?")

arvo = float(input("Mikä on hemoglobiiniarvosi?"))

if sukupuoli== "Nainen" and arvo <117:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli== "Nainen" and arvo > 175:
    print("Hemoglobiiniarvo on korkea.")
elif sukupuoli== "Nainen" and 117 <= arvo < 175:
    print("Hemoglobiiniarvo on normaali.")

elif sukupuoli== "Mies" and arvo < 134:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli== "Mies" and arvo> 195:
    print("Hemoglobiiniarvo on korkea.")
elif sukupuoli== "Mies" and 134 <= arvo < 195:
    print("Hemoglobiiniarvo on normaali.")

#4 tehtava

vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"Vuosi {vuosi} on karkausvuosi.")

else: print(f"Vuosi {vuosi} ei ole karkausvuosi.")

