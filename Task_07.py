import RPi.GPIO as GPIO    #Importe la bibliothèque GPIO pour contrôler les broches du Raspberry Pi
import time    #Importe la bibliothèque time pour gérer les temporisations

# Configuration des broches GPIO
CLK = 12    #Broche connectée au signal d'horloge (CLK)
DT = 11    #Broche connectée au signal de données (DT)
SW =13    #Broche connectée au bouton poussoir intégré à l'encodeur

def setup():
    GPIO.setmode(GPIO.BOARD)    #Utilise la numérotation physique des broches (1 à 40)
    #Configure chaque broche comme une entrée avec résistance de tirage vers le haut
    GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
    compteur = 0    #Initialise le compteur à zéro
    dernier_etat_clk = GPIO.input(CLK)    #Mémorise l’état initial de CLK
    while True:
        clk_state = GPIO.input(CLK)    #Lecture actuelle de CLK
        dt_state = GPIO.input(DT)    #Lecture actuelle de DT
        sw_state = GPIO.input(SW)    #Lecture de l'état du bouton-poussoir

        if clk_state != dernier_etat_clk:    #Si l'état de CLK a changé, cela signifie un mouvement de l'encodeur
            if dt_state != clk_state:    #Vérifie la direction de rotation
                compteur += 1    #Rotation dans un sens : incrémentation
                print("Compteur:", compteur)
            else:
                compteur -= 1    #Rotation dans l'autre sens : décrémentation
                print("Compteur:", compteur)
                
        if sw_state == GPIO.LOW:    #Si le bouton poussoir est pressé (état bas), on réinitialise le compteur
            compteur = 0
            print("Reset du compteur")
            print("0")
            time.sleep(0.3)  #Délai pour éviter les rebonds du bouton

        dernier_etat_clk = clk_state    #Met à jour l’état précédent
        time.sleep(0.01)  # petite pause pour éviter les rebonds

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
