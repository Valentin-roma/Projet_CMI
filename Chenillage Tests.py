#Code permettant le clignotage d'une ligne de LED (chenillage)

import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time

#Led = Port (defini le port a laquelle la led est connecté)
led1 = 22
led2 = 12
led3 = 18
led4 = 16
led5 = 11
led6 = 13
led7 = 7
led8 = 15

def setup():
    GPIO.setmode(GPIO.BOARD)#Définit le mode de numération des broches en mode BOARD (numérotation physique)
    GPIO.setup(led1,GPIO.OUT)#Configure la broche dee la LED1 comme une sortie 
    GPIO.setup(led2,GPIO.OUT)#Configure la broche dee la LED2 comme une sortie 
    GPIO.setup(led3,GPIO.OUT)#Configure la broche dee la LED3 comme une sortie 
    GPIO.setup(led4,GPIO.OUT)#Configure la broche dee la LED4 comme une sortie 
    GPIO.setup(led5,GPIO.OUT)#Configure la broche dee la LED5 comme une sortie 
    GPIO.setup(led6,GPIO.OUT)#Configure la broche dee la LED6 comme une sortie 
    GPIO.setup(led7,GPIO.OUT)#Configure la broche dee la LED7 comme une sortie 
    GPIO.setup(led8,GPIO.OUT)#Configure la broche dee la LED8 comme une sortie 



def main():
    while True:
        GPIO.output(led1, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led1,GPIO.HIGH)

        GPIO.output(led2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led2,GPIO.HIGH)

        GPIO.output(led3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led3,GPIO.HIGH)

        GPIO.output(led4, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led4,GPIO.HIGH)

        GPIO.output(led5, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led5,GPIO.HIGH)

        GPIO.output(led6, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led6,GPIO.HIGH)

        GPIO.output(led7, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led7,GPIO.HIGH)

        GPIO.output(led8, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led8,GPIO.HIGH)



        



        
            
























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
