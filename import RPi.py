import RPi.GPIO as GPIO
import time


DS = 17       # Broche de données (DS) du 74HC595
SH_CP = 27    # Broche d'horloge de décalage (SH_CP)
ST_CP = 22    # Broche d'horloge de stockage (ST_CP)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DS, GPIO.OUT)
GPIO.setup(SH_CP, GPIO.OUT)
GPIO.setup(ST_CP, GPIO.OUT)
numéro = { 0: 0b00111111, 1: 0b00000110, 2: 0b01011011, 3: 0b01001111, 4: 0b01100110, 5: 0b01101101, 6: 0b01111101, 7: 0b00000111, 8: 0b01111111, 9: 0b01101111 }

def shift_out(data):
    for i in range(7, -1, -1):  # Envoie du bit le plus significatif au moins significatif
        bit = (data >> i) & 1
        GPIO.output(DS, bit)
        GPIO.output(SH_CP, GPIO.HIGH)  # Front montant pour décaler
        GPIO.output(SH_CP, GPIO.LOW)
    GPIO.output(ST_CP, GPIO.HIGH)      # Latch pour transférer vers les sorties
    GPIO.output(ST_CP, GPIO.LOW)


try:
    while True:
        for i in range(10):
            shift_out(numéro[i])       # Afficher le chiffre i
            time.sleep(1)              # attend d'une seconde entre les chiffres

except KeyboardInterrupt:
    destroy()
finally:
    print("destroy")
    destroy()                     
