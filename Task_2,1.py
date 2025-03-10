#Chenillage de LED 

import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time
nmbreled = [22,12,18,16,11,13,7,15] #Liste des ports de chaque LED connecté (rangés par ordre du chenillage)
def setup():
    GPIO.setmode(GPIO.BOARD)
    for led in nmbreled:
        GPIO.setup(led, GPIO.OUT)


def main():
    while True: #définit une condition de boucle toujours vraie   
        for led in nmbreled: #parcourt la liste des LED et associe a led une valeur de nmbreled
            GPIO.output(led, GPIO.LOW)# Allume la LED
            time.sleep(0.05) # Attend 0.05 seconde
            GPIO.output(led,GPIO.HIGH)# Éteint la LED
        for i in range(len(nmbreled)-1,-1,-1):#parcourt la liste des LED en sens inverse
            led=nmbreled[i]# associe a led la valeur actuelle de la boucle afin de parcourir la boucle en inverse
            GPIO.output(led,GPIO.LOW) # Allume la LED
            time.sleep(0.05)# Attend 0.05 seconde
            GPIO.output(led,GPIO.HIGH) # Éteint la LED







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
