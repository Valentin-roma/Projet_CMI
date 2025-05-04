import RPi.GPIO as GPIO
import time

nmbreled = [22,12,18,16,11,13,7,15] #liste des ports pour chaque LED
bouton = 32  #numéro de port pour le bouton

etat_led = False #état initial des leds


def setup():
    GPIO.setmode(GPIO.BOARD)  #Utilise la numérotation BOARD
    GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #initialise le bouton en bas comme 0
    for led in nmbreled:#boucle qui passe par chaque led pour les initialiser comme éteinte
        GPIO.setup(led, GPIO.OUT)#initialise les leds
        GPIO.output(led, GPIO.LOW)  #toutes les leds sont éteintes au démarrage

def verification(x):
    global etat_led
    if GPIO.input(x) == GPIO.LOW:  #Si le bouton est pressé (LOW en mode pull-up)
        etat_led = not etat_led #inverse l'état des leds selon l'appui du bouton

def main():
    GPIO.add_event_detect(bouton,GPIO.BOTH,callback=verification) #attend l'événement de l'appui du bouton pour appeler la fonction verification au dessus
    while True:#boucle infinie
        if verification: #si le bouton est pressé
            for led in nmbreled: #parcourt la liste des LED et associe a led une valeur de nmbreled
                if not verification:#verfie si le bouton est pressé durant le cycle
                    break#sort de la boucle
                GPIO.output(led, GPIO.LOW) #allume la LED
                time.sleep(0.05) # Attend 0.05 seconde
                GPIO.output(led,GPIO.HIGH) #éteint la LED
            for i in range(len(nmbreled)-1,-1,-1):#parcourt la liste des LED en sens inverse
                led=nmbreled[i]# associe a led la valeur actuelle de la boucle afin de parcourir la boucle en inverse
                GPIO.output(led,GPIO.LOW) #allume la LED
                time.sleep(0.05)#attend 0.05 seconde
                GPIO.output(led,GPIO.HIGH) #éteint la LED
    time.sleep(0.1)#attend 0.1 seconde

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
