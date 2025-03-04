#Test

import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time
nmbreled = [22,12,18,16,11,13,7,15] #Liste des ports pour chaque LED
bouton = 32

def setup():
    GPIO.setmode(GPIO.BOARD)#Définit le mode de numération des broches en mode BOARD (numérotation physique)
    GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for led in nmbreled:#Parcours la liste et prend chaque valeur de celle-ci sous la variable led
        GPIO.setup(led, GPIO.OUT)#Configure la broche de chaque LED comme une sortie
 


def my_callback(bouton):#Fonction de rappel executé lorsqu'un évènement est détecté
    """Callback exécuté lorsqu'un appui sur le bouton est détecté"""
    GPIO.output(led,GPIO.LOW)#Eteint la LED lorsque l'évènement est détecté



def main():
    GPIO.add_event_detect(bouton, GPIO.FALLING, callback=my_callback)#détecte un appui sur le bouton (flanc montant) et appelle my_callback
    while True:
        if GPIO.event(bouton):#vérifie si un évenement a été détecté sur le bouton
            GPIO.output(led,GPIO.HIGH)#Allume la LED
            for led in nmbreled: #Parcours la liste et prend chaque valeur de celle-ci sous la variable led
                GPIO.output(led, GPIO.LOW)#Allume la LED lorsque l'évènement est détecté
                time.sleep(0.05) #Mets un temps d'arrêt
                GPIO.output(led,GPIO.HIGH)#Eteindre la LED lorsque l'évènement est détecté

            for i in range(len(nmbreled)-1,-1,-1): #Parcours la liste en l'inversant 
                led=nmbreled[i] #Associe a chaque itération une i-eme variable de nmbreled a led
                GPIO.output(led,GPIO.LOW)#Allume la LED lorsque l'évènement est détecté
                time.sleep(0.05) #Mets un temps d'arrêt
                GPIO.output(led,GPIO.HIGH)#Eteint la LED lorsque l'évènement est détecté

                


                    
                        
        

























def destroy():
    #Turn Off LED
    #GPIO.output(ledPin, GPIO.LOW)
    #Release resource
    GPIO.cleanup()

#If run this script directly, do:
if __name__ == '__main__':
    destroy()
    setup()
    try:
        main()
    #When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed
    except KeyboardInterrupt:
        destroy()
    finally:
        print("destroy")
        destroy()