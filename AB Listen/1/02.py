zahlenliste = [] 

while(True):
    kommand = input('Bitte geben sie iwas ein: ')
    
    if(kommand == 'Ende'):
        break
    
    elif(kommand == 'Einfügen'): 
        zahl = int(input('Bitte geben sie eine Zahl ein: '))
        zahlenliste.append(zahl)
        
    elif(kommand == 'Ausgeben'):
        print(zahlenliste)        
        
    elif(kommand == 'Länge'):
        laenge = len(zahlenliste)
        print(laenge)
        
    elif(kommand == 'LöscheZahlAnPosition'):
        index = int(input('Bitte geben sie ein Position ein: '))
        laenge = len(zahlenliste)
        
        if(index >= laenge):
            print('Diese Position gibt es nicht :D')
            
        else:
            zahlenliste.remove(index)
    
    elif(kommand == 'LöscheAlleZahlen'):
        zahlenliste.clear()    
    else:
        print('sie haben was falsches eingegeben :D')
    