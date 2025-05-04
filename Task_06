
import RPi.GPIO as GPIO #importe la bibliotheque RPIO.GPIO pour controler la carte
import time #importe la bibliotheque time
buzzer=11                                                                                   
  
def setup():
    GPIO.setmode(GPIO.BOARD)#Définit le mode de numération des broches en mode  physique)
    GPIO.setup(buzzer,GPIO.OUT)#Configure la broche dee la LED comme une sortie 

   
def main():
    GPIO.output(buzzer,GPIO.LOW) #definit le buzzer en LOW
    while True: #définit une condition toujours vraie
            GPIO.output(buzzer,GPIO.HIGH) #allume le buzzer
            time.sleep(0.1)  #attendre 0.1 seconde
            GPIO.output(buzzer,GPIO.LOW) #éteint le buzzer 
            time.sleep(0.1) #attend 0.1 seconde
    time.sleep(0.5) #attend 0.5 seconde

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
