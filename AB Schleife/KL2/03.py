import random

meineZufallszahl = random.randint(0,100)
vermutung = 0

while True:
    
    vermutung = int(input("Rate mal: "))
    
    if(vermutung < meineZufallszahl):
        print("Zu klein. Try again :)")
        
    elif(vermutung > meineZufallszahl):
        print("Zu groß. Try again :)")
        
    else:
        print("gg, wp :D")
        break