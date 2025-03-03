#!/usr/bin/env python3
import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time
led = 11   #defini le port a laquelle la led est connecté
bouton = 12 #defini le port a laquelle la led est connecté

def setup():
    GPIO.setmode(GPIO.BOARD)#Définit le mode de numération des broches en mode BOARD (numérotation physique)
    GPIO.setup(led,GPIO.OUT)#Configure la broche dee la LED comme une sortie 
    GPIO.setup(bouton,GPIO.IN)#Configure la broche du bouton comme une entrée


def main():
    while True:
        if GPIO.input(bouton)==GPIO.LOW:
            GPIO.output(led, GPIO.LOW)
            print("la led s'allume !")
        else:
            GPIO.output(led, GPIO.HIGH)
            print("la led s'éteint !")







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
