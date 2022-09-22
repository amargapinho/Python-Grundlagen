eingabe = input("bitte geben sie ein Zahl ein")
zahl = int(eingabe)

summe = 0

for i in range(1, zahl):
    summe = i+summe

print(summe)