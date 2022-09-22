summe = 0 
notenAnzahl = 0
eingabe = ""

while True:
    eingabe = input("Bitte geben sie eine Schulnote ein: ")    
    if(eingabe == "Ende" or eingabe == "ende"):
        break
    
    schulnote = int(eingabe)
    
    if(schulnote < 1 or schulnote > 6):
        print("Keine gültige Schulnote. Bitte erneut versuchen :)")
        
    else:
        summe = summe + schulnote
        notenAnzahl = notenAnzahl + 1
        
    notenschnitt = summe / notenAnzahl
    print("Der Notenschnitt ist " , notenschnitt)