zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

def ermitlleKleinsteZahlInListe (liste):
    bisherKleinsteZahl = liste[0]
    for zahl in liste:
        if zahl < bisherKleinsteZahl:
            bisherKleinsteZahl = zahl
    
    return bisherKleinsteZahl

print(ermitlleKleinsteZahlInListe(zahlenliste))