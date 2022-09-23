# Diese Funktion adiert alle Zahlen einer Liste 
def summiereAlleZahlenInListe (liste):
    zwischensumme = 0
    
    for zahl in liste:
        zwischensumme = zwischensumme + zahl 
    return zwischensumme

# Diese Funktion ermittelt die größte Zahl einer Liste
def ermittleGroesseteZahlInListe (liste):
    bisherGroessteZahl = liste[0]
    for zahl in liste:
        if zahl > bisherGroessteZahl:
            bisherGroessteZahl = zahl
    return bisherGroessteZahl

# Unsere Beispielzahlenliste
zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

# Nun testen wir beide Funktionen mit unserer Beispielliste
summeDerZhalenliste = summiereAlleZahlenInListe(zahlenliste)
print("Die Summe aller Zahlen in der Zahlenliste ist " + str(summeDerZhalenliste))

groessteZahlInZahlenliste = ermittleGroesseteZahlInListe(zahlenliste)
print("Die größte Zahl in der Zahlenliste ist " + str(groessteZahlInZahlenliste))