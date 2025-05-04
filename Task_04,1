import RPi.GPIO as GPIO  #importe la bibliothèque RPi.GPIO
import time  #importe la bibliothèque time

led = 12  #broche GPIO pour la LED
bouton = 16  #broche GPIO pour le bouton poussoir

i = 0  #rapport cyclique initial (0%)
sens = 1  #sens de variation du rapport cyclique

def setup():
    GPIO.setmode(GPIO.BOARD)  #utilise la numérotation physique des broches (BOARD)
    GPIO.setup(led, GPIO.OUT)  #configure la broche de la LED comme une sortie
    GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #configure le bouton en entrée avec résistance de pull-up
    p = GPIO.PWM(led, 1000) #crée une instance PWM avec une fréquence initiale de 1000 Hz
    p.start(i)  #démarre le PWM avec le rapport cyclique initial

def presse(btn):
    if GPIO.input(btn) == GPIO.LOW:  #si le bouton est pressé
        i =i + 10 * sens #augmente ou diminue le rapport cyclique de 10%
        if i > 100:  #si le rapport cyclique dépasse 100%
            sens = -1  #change le sens de variation
        elif i < 0:  #si le rapport cyclique est inférieur à 0%
            sens = 1  #change le sens
        p.ChangeDutyCycle(i) #met à jour le rapport cyclique du PWM

def main():
    GPIO.add_event_detect(bouton, GPIO.FALLING, callback=presse, bouncetime=300) #configure une interruption sur le flanc descendant
        while True:  #boucle  infinie
            time.sleep(0.1) #délai
        p.stop() #stop le pwm







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
