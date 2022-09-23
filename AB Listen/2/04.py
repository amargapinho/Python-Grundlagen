zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

def ermittleIndexDerKleinsteZahl (liste):
    bisherKleinsteZahl = liste[0]
    for zahl in liste:
        if zahl < bisherKleinsteZahl:
            bisherKleinsteZahl = zahl

    index = liste.index(bisherKleinsteZahl)
   
def ermittleIndexDerKleinsteZahl1 (liste): 
    bisherKleinsteZahl = liste[0]
    index = 0
    
    for zahl in range(len(liste)):
        if (liste[zahl] < bisherKleinsteZahl):
            bisherKleinsteZahl = liste[zahl]
            index = zahl
    
    return index