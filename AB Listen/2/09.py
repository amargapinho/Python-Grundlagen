zahlenliste = [5, 2, 9, -13, -16, 27, -1, -67, -12, -56]

def mehrPositiveOderNegativeZahlen(liste):
    
    negativeZahlen = 0
    positiveZahlen = 0
    
    for zahl in liste:
        if(zahl<0):
            negativeZahlen = negativeZahlen + 1
            
        else:
            positiveZahlen = positiveZahlen + 1 
            
    if(positiveZahlen < negativeZahlen):
        return "Die Liste hat mehr negative als positive Zahlen"
    
    elif(positiveZahlen > negativeZahlen):
        return "Die Liste hat mehr positive als negative Zahlen"
    
    else:
        return "Die Liste hat gleich viele positive und negative Zahlen"


print (mehrPositiveOderNegativeZahlen(zahlenliste))
        
        
    