fahrtMZWI = 5
bahncard50 = 200
bahncard25 = 50

fahrtAnzahl = int(input("Wie viel Fahrten von Mainz nach Wiesbaden und zurück plannen sie?"))

kostenOhneBahncard = fahrtAnzahl * fahrtMZWI

kostenBahncard50 = kostenOhneBahncard * 0.50 + bahncard50

kostenBahncard25 = kostenOhneBahncard * 0.75 + bahncard25

print(fahrtAnzahl, "Fahrten kosten ohne Bahncard", kostenOhneBahncard, "€")
print(fahrtAnzahl, "Fahrten kosten mit Bahncard 50", kostenBahncard50, "€")
print(fahrtAnzahl, "Fahrten kosten mit Bahncard 25", kostenBahncard25, "€")

input()