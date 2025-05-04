import RPi.GPIO as GPIO
import time

# Configuration des broches GPIO
CLK = 12   
DT = 11   
SW =13
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
    compteur = 0
    dernier_etat_clk = GPIO.input(CLK)
    while True:
        clk_state = GPIO.input(CLK)
        dt_state = GPIO.input(DT)
        sw_state = GPIO.input(SW)

        if clk_state != dernier_etat_clk:
            if dt_state != clk_state:
                compteur += 1
                print("Compteur:", compteur)
            else:
                compteur -= 1
                print("Compteur:", compteur)
        if sw_state == GPIO.LOW:
            compteur = 0
            print("Reset du compteur")
            print("0")
            time.sleep(0.3)  # Anti-rebond

        dernier_etat_clk = clk_state
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
