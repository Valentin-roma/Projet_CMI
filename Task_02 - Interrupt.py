import RPi.GPIO as GPIO  # Importation de la bibliothèque pour contrôler les GPIO
import time  # Importation de la bibliothèque pour gérer les délais


led = 12  # Broche  pour la LED
bouton = 16  # Broche pour le bouton 

def setup():
    GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation des broches en BOARD
    GPIO.setup(led, GPIO.OUT)  # Configure la broche de la LED comme une sortie
    GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Configure le bouton en entrée avec résistance de pull-up

def presse(btn):
    if GPIO.input(btn) == GPIO.HIGH:#Si le bouton est pressé (état LOW)
        GPIO.output(led, GPIO.HIGH)  #Allumer la LED
    else:  #Si le bouton est relâché
        GPIO.output(led, GPIO.LOW)  #Éteindre la LED

def main():
    GPIO.add_event_detect(bouton, GPIO.BOTH, callback=presse, bouncetime=200)  # Détection d'événement avec anti-rebond
    GPIO.output(led, GPIO.HIGH)  # Allumer la LED au démarrage
    while True: #Boucle infinie
        time.sleep(1) #Délai

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
