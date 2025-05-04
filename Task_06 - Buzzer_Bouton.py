
import RPi.GPIO as GPIO    #importe la bibliotheque RPIO.GPIO pour controler la carte
import time    #importe la bibliotheque time
buzzer=11                                                                                   
bouton=12
etat_buzz=False    #Etat de la LED
def setup():
    GPIO.setmode(GPIO.BOARD)    #Définit le mode de numération des broches en mode  physique)
    GPIO.setup(buzzer,GPIO.OUT)    #Configure la broche dee la LED comme une sortie 
    GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Initialise le bouton en bas comme 0
   

def verification(x):
    global etat_buzz #definti une vaariable global
    if GPIO.input(x) == GPIO.LOW:    # Si le bouton est pressé (LOW en mode pull-up)
        etat_buzz = not etat_buzz    # Inverse l'état des leds selon l'appui du bouton

def main():
    GPIO.add_event_detect(bouton,GPIO.BOTH,callback=verification,bouncetime=300)    # Attend l'événement de l'appui du bouton pour appeler la fonction verification au dessus
    GPIO.output(buzzer,GPIO.LOW)
    while True:    #définit une condition toujours vraie
        if verification:    # Si le bouton est pressé
            GPIO.output(buzzer,GPIO.HIGH)    # Allume le buzzer
            time.sleep(0.1)    # Attendre 0.1 seconde
            GPIO.output(buzzer,GPIO.LOW)    # Éteint le buzzer
            time.sleep(0.1) #attend 0.1 
        time.sleep(0.5) #attend 0;5

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
