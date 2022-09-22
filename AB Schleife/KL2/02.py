eingabe = ""

while True:
    eingabe = input("Bitte geben sie ein Bundesland ein: ")
    
    if(eingabe == "Baden-Wüttemberg"):
        print("Stuttgart.")
        
    elif(eingabe == "Bayern"):
        print("München.")
        
    elif(eingabe == "Berlin"):
        print("Berlin.")
        
    elif(eingabe == "Brandenburg"):
        print("Potsdam.")
        
    elif(eingabe == "Bremen"):
        print("Bremen.")
        
    elif(eingabe == "Hamburg"):
        print("Hamburg.")
        
    elif(eingabe == "Hessen"):
        print("Wiesbaden.")
        
    elif(eingabe == "Mecklenburg-Vorpommen"):
        print("Schwerin.")
        
    elif(eingabe == "Niedersachsen"):
        print("Hannover.")
    
    elif(eingabe == "Nordrhein-Westfalen"):
        print("Düsseldorf.")
        
    elif(eingabe == "Rheinland-Pfalz"):
        print("Mainz.")
        
    elif(eingabe == "Saarland"):
        print("Saarbrücken.")
        
    elif(eingabe == "Sachsen"):
        print("Dresden.")
        
    elif(eingabe == "Sachsen-Anhalt"):
        print("München.")

    elif(eingabe == "Schleswig-Holstein"):
        print("Kiel.")
    
    elif(eingabe == "Thüringen"):
        print("Erfurt.")
        
    elif(eingabe == "Ende" or eingabe == "ende"):
        break
        
    else:
        print("Das ist kein Bundesland :)")
    