import RPi.GPIO as GPIO  # Importe la bibliothèque RPi.GPIO 
import time  # Importe la bibliothèque time


led = 12
freq = 1000 

def setup():
    GPIO.setmode(GPIO.BOARD)  # Utilise la numérotation physique des broches (BOARD)
    GPIO.setup(led, GPIO.OUT)  # Configure la broche de la LED comme une sort

def main():
        p = GPIO.PWM(led, freq) #creer l'instance pwm
        p.start(0)  # Démarre le PWM avec un rapport cyclique de 0% (LED éteinte)
        while True:
            for i in range(0, 101, 1):  # 0 à 100, pas de 1
                p.ChangeDutyCycle(i)  # Change le rapport cyclique
                time.sleep(0.05)  # Délai
            print("Boucle 1")
            for i in range(100, -1, -1):  # 100 à 0, pas de -1
                p.ChangeDutyCycle(i)  # Change le rapport cyclique
                time.sleep(0.05)  # Délai
            p.stop()  # Arrête le PWM
        


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
