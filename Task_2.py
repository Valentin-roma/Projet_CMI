#!/usr/bin/env python3
#CODE Bouton - LED

import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time
led = 11   #defini le port a laquelle la led est connecté
bouton = 12 #defini le port a laquelle la led est connecté

def setup():
    GPIO.setmode(GPIO.BOARD)#Définit le mode de numération des broches en mode BOARD (numérotation physique)
    GPIO.setup(led,GPIO.OUT)#Configure la broche dee la LED comme une sortie 
    GPIO.setup(bouton,GPIO.IN)#Configure la broche du bouton comme une entrée

#Interruptions
def main(): 
    while True: #boucle infinie
        if GPIO.input(bouton)==GPIO.LOW: #Si le bouton est préssé
            GPIO.output(led, GPIO.LOW) #Alors la LED s'allume (LOW pour qu'il y ait une différence de potentiel)
            print("la led s'allume !")
        else:
            GPIO.output(led, GPIO.HIGH) #Sinon la LED s'éteint (HIGH pour que la différence de potentiel soit nulle)
            print("la led s'éteint !")
#Polling
def my_callback(channel):
    if GPIO.input(bouton) == GPIO.LOW:  # Si le bouton est pressé
        GPIO.output(led, GPIO.LOW)  # Allume la LED
        print("La LED s'allume !")
    else: #sinon
        GPIO.output(led, GPIO.HIGH)  # Éteint la LED
        print("La LED s'éteint !")

def main():
    GPIO.add_event_detect(bouton, GPIO.FALLING, callback=my_callback)# Configurer une interruption sur le flanc descendant (appui sur le bouton)
    try:
        while True:  # Boucle permmetant que le programme ne s'arrete pas 
            time.sleep(1)  #attendre





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
