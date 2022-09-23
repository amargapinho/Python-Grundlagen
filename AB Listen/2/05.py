zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]


def gibVerdoppelteListeZurueck (zahlenliste):
    
    neueliste = []
    
    for zahl in zahlenliste:
        
        neueZahl = zahl * 2
        neueliste.append(neueZahl)
        
    return neueliste


print(gibVerdoppelteListeZurueck(zahlenliste))
        