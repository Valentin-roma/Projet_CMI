#!/usr/bin/env python3
import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time
led = 11   #defini le port a laquelle la led est connecté
bouton = 12 #defini le port a laquelle la led est connecté

def setup():
    GPIO.setmode(GPIO.BOARD)#Définit le mode de numération des broches en mode BOARD (numérotation physique)
    GPIO.setup(led,GPIO.OUT)#Configure la broche dee la LED comme une sortie 
    GPIO.setup(bouton,GPIO.IN)#Configure la broche du bouton comme une entrée

"""def main():
    while True:
        if GPIO.input(bouton)==GPIO.HIGH:
            GPIO.output(led, GPIO.HIGH)
            print("la led s'allume !")
        else:
            GPIO.output(led, GPIO.LOW)
            print("la led s'éteint !")
"""
        
def my_callback(bouton):#Fonction de rappel executé lorsqu'un évènement est détecté
    """Callback exécuté lorsqu'un appui sur le bouton est détecté"""
    GPIO.output(led,GPIO.LOW)#Eteint la LED lorsque l'évènement est détecté

def main():
    GPIO.add_event_detect(bouton, GPIO.RISING, callback=my_callback)#détecte un appui sur le bouton (flanc montant) et appelle my_callback
    if GPIO.event(bouton):#vérifie si un évenement a été détecté sur le bouton
        GPIO.output(led,GPIO.HIGH)#Allume la LED


"""
GPIO.setup(led, GPIO.OUT)
GPIO.setup(bouton, GPIO.IN)

valeur = GPIO.input(bouton)
GPIO.output(led, 1)

if GPIO.input(bouton):
    print('Input was HIGH')

else:
    print('Input was LOW')

while GPIO.input(bouton) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things


def my_callback(bouton):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

#add rising edge detection on a channel, ignoring further edges for 200ms for switch bounce handling
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)
"""

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




       