# Liste erstellen 
from operator import truediv


fantasieGegenstaende = ['einhorn', 'zwerg', 'fee']

# Liste ausgeben 
print(fantasieGegenstaende)

# Wert für Wert ausgeben 
for ggstnd in fantasieGegenstaende:
    print(ggstnd)
    
#  Elemente hinzufügen 
fantasieGegenstaende.append('bielefeld')

# Mehrere Elemente hinzufügen
fantasieGegenstaende.extend(['hexe', 'drache', 'zentaur', 'phoenix', 'harpyie'])

# Elemente in einem bestimmten Index hinzufügen
fantasieGegenstaende.insert(3, 'elfen')

# Elemente löschen
fantasieGegenstaende.remove('bielefeld')

# Elemente sortieren
fantasieGegenstaende.sort()
fantasieGegenstaende.sort(reverse = True)
sorted(fantasieGegenstaende, reverse = True)




